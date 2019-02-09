# Python Bitfinex API client

---
This is a simple Python client for the Bitfinex REST API (V1 and V2). It supports public as well as private endpoints.

---
## Installation

You can either clone the repository directly from the Github webpage or run the following command(s) in your terminal:

Pip Installation:
```
pip install bitfinex-tencars
```

Alternatively you can clone the Git repository:
```
git clone https://github.com/akcarsten/bitfinex_api.git
```

Then go to the folder to which you cloned the repository and run:

```
python setup.py install
```

Now you can run Python and import the Bitfinex client.

---
## Examples of how to use the interface

### Public endpoints
Public endpoints can be used without entering any keys as shown in the examples below.

#### Example 1: Retrieving current tick data
```python
import bitfinex

# Initialize the api
api = bitfinex.api_v1()

# Select a trading pair
pair = 'btcusd'

# Get the current ticker data for the pair
api.ticker(pair)
```

#### Example 2: Available currency pairs
```python
import bitfinex

# Initialize the api
api = bitfinex.api_v1()

# Get all available currency pairs
symbols = api.symbols()
```

All available public endpoints are included in this client. For a full documentation check the Bitfinex API [webpage](
https://docs.bitfinex.com/docs/public-endpoints)

### Private endpoints
In order to use private endpoints the public- and secrete keys need to be provided while initializing the API as shown in the example below in which the current account balance can be retrieved.

#### Example 1: Check account balance
```python
import bitfinex

key = 'YOUR_PUBLIC_KEY'
secrete = 'YOUR_SECRETE_KEY'

api = bitfinex.api_v1(key, secrete)
my_balance = api_bitfinex.balance()
```

#### Example 2: Place an buy order
```python
import bitfinex

symbol = 'btcusd'        # Currency pair to trade
amount = '0'             # Amount to buy
price = '0'              # Buy price
side = 'buy'             # Buy or sell
type = 'exchange market' # Which type

# Send the order
api.place_order(symbol, amount, price, side, type)
```

---
## Further information

For a full documentation of all API commands and what parameters are needed to run them, check out the Bitfinex API documentation for [public endpoints](https://docs.bitfinex.com/docs/public-endpoints) and the documentation for the [private endpoints](https://docs.bitfinex.com/docs/rest-auth) of the V1 API.

For the V2 API you can find the reference [here](https://docs.bitfinex.com/v2/reference).

All endpoints should be included in this API. In case of changes or bugs please let me know.
