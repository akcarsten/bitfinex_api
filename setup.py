from setuptools import setup

setup(
    name='bitfinex',
    version='1.2',
    packages=['bitfinex'],
    url='https://github.com/akcarsten/bitfinex',
    license='',
    author='Carsten Klein',
    author_email='https://www.linkedin.com/in/carsten-klein/',
    description='Bitfinex REST API client'
)

# Import libraries
import requests
import json

# Define function
def candles(symbol='BTCUSD', interval='1m'):
    url = 'https://api.bitfinex.com/v2/candles/' \
          'trade:{}:t{}/hist'.format(interval, symbol)
    return requests.get(url).json()

# Request Bitcoin/USD data
ohlc = candles()
