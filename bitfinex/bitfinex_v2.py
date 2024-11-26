import time
import requests
import json
import hmac
import hashlib


class api_v2(object):
    _api_url = 'https://api.bitfinex.com'
    _api_key = ''
    _api_secret = ''
    _api_nonce = ''

    # Init class
    def __init__(self, api_key=None, api_secret=None):
        if api_key is None and api_secret is None:
            print('No keys, only access to public API functions')
        else:
            self._api_key = api_key
            self._api_secret = api_secret

    # create nonce
    @staticmethod
    def _nonce():
        return str(int(round(time.time() * 1000)))

    def _headers(self, path, nonce, body):

        signature = '/api' + path + nonce + body
        print('Signing: ' + signature)

        h = hmac.new(self._api_secret.encode('utf-8'), signature.encode('utf-8'), hashlib.sha384)
        signature = h.hexdigest().lower()

        return {
            'bfx-nonce': nonce,
            'bfx-apikey': self._api_key,
            'bfx-signature': signature,
            'content-type': 'application/json'
        }

    # create signature
    def api_call(self, method, param={}):
        url = self._api_url + method
        nonce = self._nonce()
        raw_body = json.dumps(param)
        headers = self._headers(method, nonce, raw_body)

        # return requests.post(url, data={}, headers=headers)
        return requests.post(url, headers=headers, data=raw_body, verify=True)

    # Public endpoints
    @staticmethod
    def tickers(symbol='btcusd'):
        if type(symbol) is str:
            symbols = 't{}'.format(symbol.upper())
        else:
            symbols = ','.join(['t{}'.format(s.upper()) for s in symbol])
        return requests.get('https://api.bitfinex.com/v2/tickers?symbols={}'.
                            format(symbols)).json()

    @staticmethod
    def ticker(symbol='btcusd'):
        return requests.get('https://api.bitfinex.com/v2/ticker/t{}'.
                            format(symbol.upper())).json()

    @staticmethod
    def trades(symbols='btcusd', limit=1000, start=None, end=None, sort=-1):
        return requests.get('https://api.bitfinex.com/v2/trades/t{}/hist?limit={}&start={}&end={}&sort={}'.
                            format(symbols.upper(), limit, start, end, sort)).json()

    @staticmethod
    def books(symbol='btcusd', precision='P0', length=100):
        return requests.get('https://api.bitfinex.com/v2/book/t{}/{}?len={}'.
                            format(symbol.upper(), precision, length)).json()

    @staticmethod
    def stats(key='funding.size', size='1m', symbol='usd', sort=-1):
        return requests.get('https://api.bitfinex.com/v2/stats1/{}:{}:f{}/hist?sort={}'.
                            format(key, size, symbol.upper(), sort)).json()

    @staticmethod
    def candles(symbol='btcusd', interval='1m', limit=1000, start=None, end=None, sort=-1):
        return requests.get('https://api.bitfinex.com/v2/candles/trade:{}:t{}/hist?limit={}&start={}&end={}&sort={}'.
                            format(interval, symbol.upper(), limit, start, end, sort)).json()

    # REST calculation endpoints
    @staticmethod
    def market_average_price(symbol='btcusd', amount=1.123, period='', rate_limit=''):
        url = 'https://api.bitfinex.com/v2/calc/trade/avg'
        querystring = {'symbol': 't'+str(symbol).upper(),
                       'amount': str(amount),
                       'period': str(period),
                       'rate_limit': str(rate_limit)}
        return requests.request('POST', url, params=querystring).json()

    @staticmethod
    def forex(ccy1='eur', ccy2='usd'):
        url = 'https://api.bitfinex.com/v2/calc/fx'
        querystring = {'ccy1': ccy1.upper(),
                       'ccy2': ccy2.upper()}
        return requests.request('POST', url, params=querystring).json()

    # Private endpoints
    def wallets(self):
        return self.api_call('/v2/auth/r/wallets', {}).json()

    def orders(self, symbol='btcusd', start=1545079680000, end=1545019080000, limit=25, sort=-1):
        querystring = {'symbol': 't'+str(symbol).upper(),
                       'start': str(start),
                       'end': str(end),
                       'limit': str(limit),
                       'sort': str(sort)}
        return self.api_call('/v2/auth/r/orders/t{}/hist'.format(symbol.upper()), querystring).json()

    def order_trades(self, symbol='btcusd', order_id=''):
        return self.api_call('/v2/auth/r/order/t{}:{}/trades'.format(symbol.upper(), order_id), {}).json()

    def positions(self):
        return self.api_call('/v2/auth/r/positions', {}).json()

    def funding_offers(self, symbol='btcusd'):
        return self.api_call('/v2/auth/r/funding/offers/t{}'.format(symbol.upper()), {}).json()

    def funding_offers_history(self, symbol='btcusd', start=1545079680000, end=1545019080000, limit=25):
        querystring = {'symbol': 't'+str(symbol).upper(),
                       'start': str(start),
                       'end': str(end),
                       'limit': str(limit)}
        return self.api_call('/v2/auth/r/funding/offers/t{}/hist'.format(symbol.upper()), querystring).json()

    def loans(self, symbol='btcusd'):
        return self.api_call('/v2/auth/r/funding/loans/t{}'.format(symbol.upper()), {}).json()

    def loans_history(self, symbol='btcusd', start=1545079680000, end=1545019080000, limit=25):
        querystring = {'symbol': 't'+str(symbol).upper(),
                       'start': str(start),
                       'end': str(end),
                       'limit': str(limit)}
        return self.api_call('/v2/auth/r/funding/loans/t{}/hist'.format(symbol.upper()), querystring).json()

    def credits(self, symbol='btcusd'):
        return self.api_call('/v2/auth/r/funding/credits/t{}'.format(symbol.upper()), {}).json()

    def credits_history(self, symbol='btcusd', start=1545079680000, end=1545019080000, limit=25):
        querystring = {'symbol': 't'+str(symbol).upper(),
                       'start': str(start),
                       'end': str(end),
                       'limit': str(limit)}
        return self.api_call('/v2/auth/r/funding/credits/t{}/hist'.format(symbol.upper()), querystring).json()

    def funding_trades(self, symbol='btcusd', start=1545079680000, end=1545019080000, limit=25):
        querystring = {'symbol': 't'+str(symbol).upper(),
                       'start': str(start),
                       'end': str(end),
                       'limit': str(limit)}
        return self.api_call('/v2/auth/r/funding/trades/t{}/hist'.format(symbol.upper()), querystring).json()

    def margin_info(self, key=''):
        return self.api_call('/v2/auth/r/info/margin/{}'.format(key), {}).json()

    def funding_info(self, key=''):
        return self.api_call('/v2/auth/r/info/funding/{}'.format(key), {}).json()

    def movements(self, currency='btc'):
        return self.api_call('/v2/auth/r/movements/{}/hist'.format(currency.upper()), {}).json()

    def alerts(self, alert_type='price'):
        querystring = {'type': alert_type}
        return self.api_call('/v2/auth/r/alerts', querystring).json()

    def alert_set(self, alert_type='price', symbol='btc', price=1000.0):
        querystring = {'type': alert_type,
                       'symbol': symbol.upper(),
                       'price': str(price)}
        return self.api_call('/v2/auth/w/alert/set', querystring).json()

    def alert_delete(self, symbol='btc', price=1000.0):
        return self.api_call('/v2/auth/w/alert/price:t{}:{}/del'.format(symbol.upper(), price), {}).json()

    def calc_available_balance(self, symbol='btcusd', direction=1, rate=1, order_type='EXCHANGE'):
        querystring = {'symbol': 't'+str(symbol).upper(),
                       'dir': str(direction),
                       'rate': str(rate),
                       'type': order_type.upper()}
        return self.api_call('/v2/auth/calc/order/avail/', querystring).json()

    def ledgers(self, currency='btc'):
        return self.api_call('/v2/auth/r/ledgers/{}/hist'.format(currency.upper()), {}).json()

    def user_settings_read(self, params={}):
        return self.api_call('/v2/auth/r/settings', params).json()

    def user_settings_write(self, params={}):
        return self.api_call('/v2/auth/w/settings/set', params).json()

    def user_settings_delete(self, params={}):
        return self.api_call('/v2/auth/w/settings/del', params).json()

    def user_info(self):
        return self.api_call('/v2/auth/r/info/user', {}).json()
