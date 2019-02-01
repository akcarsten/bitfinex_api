import time
import base64
import requests
import json
import hmac
import hashlib


class api_v1(object):
    __api_url = 'https://api.bitfinex.com'
    __api_key = ''
    __api_secret = ''
    __api_nonce = ''

    # Init class
    def __init__(self, api_key=None, api_secret=None):
        if api_key is None and api_secret is None:
            print('No keys, only access to public API functions')
        else:
            self.__api_key = api_key
            self.__api_secret = api_secret

    # create nonce
    def __nonce(self):
        self.__api_nonce = str(time.time() * 100000)

    # create signature
    def api_call(self, method, param={}):
        url = self.__api_url + method

        self.__nonce()

        payload_object = {
                'request': method,
                'nonce': self.__api_nonce,
                }
        payload_object.update(param)

        payload_json = json.dumps(payload_object)
        payload = base64.b64encode(bytes(payload_json, "utf-8"))

        signature = hmac.new(self.__api_secret.encode('utf-8'), payload, hashlib.sha384).hexdigest().lower()

        # Headers
        headers = {
            'X-BFX-APIKEY': self.__api_key,
            'X-BFX-PAYLOAD': base64.b64encode(bytes(payload_json, "utf-8")),
            'X-BFX-SIGNATURE': signature
        }
        return requests.post(url, data={}, headers=headers)

    # Public endpoints
    @staticmethod
    def symbols():
        return requests.get('https://api.bitfinex.com/v1/symbols').json()

    @staticmethod
    def symbol_details():
        return requests.get('https://api.bitfinex.com/v1/symbols_details').json()

    @staticmethod
    def lends(currency='usd'):
        return requests.get('https://api.bitfinex.com/v1/lends/{}'.format(currency)).json()

    @staticmethod
    def trades(symbol='btcusd'):
        return requests.get('https://api.bitfinex.com/v1/trades/{}'.format(symbol)).json()

    @staticmethod
    def order_book(symbol='btcusd'):
        return requests.get('https://api.bitfinex.com/v1/book/{}'.format(symbol)).json()

    @staticmethod
    def funding_book(currency='usd'):
        return requests.get('https://api.bitfinex.com/v1/lendbook/{}'.format(currency)).json()

    @staticmethod
    def stats(symbol='btcusd'):
        return requests.get('https://api.bitfinex.com/v1/stats/{}'.format(symbol)).json()

    @staticmethod
    def ticker(symbol='btcusd'):
        return requests.get('https://api.bitfinex.com/v1/pubticker/{}'.format(symbol)).json()

    # Private endpoints
    def account_infos(self):
        return self.api_call('/v1/account_infos', {}).json()

    def account_fees(self):
        return self.api_call('/v1/account_fees', {}).json()

    def summary(self):
        return self.api_call('/v1/summary', {}).json()

    def deposits(self, method, wallet_name, renew):
        param = {
            'method': method,
            'wallet_name': wallet_name,
            'renew': renew
        }
        return self.api_call('/v1/deposit/new', param=param).json()

    def key_info(self):
        return self.api_call('/v1/key_info', {}).json()

    def balance(self):
        return self.api_call('/v1/balances', {}).json()

    def transfer(self, amount, currency, walletfrom, walletto):
        param = {
            'amount': amount,
            'currency': currency,
            'walletfrom': walletfrom,
            'walletto': walletto
        }
        return self.api_call('/v1/transfer', param=param).json()

    def withdraw(self, withdraw_type, walletselected, amount, address):
        param = {
            'withdraw_type': withdraw_type,
            'walletselected': walletselected,
            'amount': amount,
            'address': address
        }
        return self.api_call('/v1/withdraw', param=param).json()

    def margin_infos(self):
        return self.api_call('/v1/margin_infos', {}).json()

    def active_orders(self):
        return self.api_call('/v1/orders', {}).json()

    def order_history(self):
        return self.api_call('/v1/orders/hist', {}).json()

    def place_order(self, symbol, amount, price, side, order_type):
        param = {
            'symbol': symbol,
            'amount': amount,
            'price': price,
            'exchange': 'bitfinex',
            'side': side,
            'type': order_type
        }
        return self.api_call('/v1/order/new', param=param).json()

    def cancel_order(self, order_id):
        param = {'order_id': order_id}
        return self.api_call('/v1/order/cancel', param=param).json()

    def cancel_all(self):
        return self.api_call('/v1/order/cancel/all', {}).json()

    def order_status(self, order_id):
        param = {'order_id': order_id}
        return self.api_call('/v1/order/status', param=param).json()

    def position(self):
        return self.api_call('/v1/positions', {}).json()

    def balance_history(self, currency):
        param = {'currency': currency}
        return self.api_call('/v1/history', param=param).json()

    def movements(self, currency):
        param = {'currency': currency}
        return self.api_call('/v1/history/movements', param=param).json()

    def mytrades(self, currency):
        param = {'currency': currency}
        return self.api_call('/v1/mytrades', param=param).json()
