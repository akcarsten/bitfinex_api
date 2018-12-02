# Bitfinex API


## Examples of how to use the interface

### Public endpoints 
Public endpoints can be used without entering any keys as shown in the example below.

    api = bitfinex_api()
    api.ticker()
    
In order to use private endpoints the public- and secrete keys need to be provided while initializing the API as shown in the example below.

    api = exchange_apis.get_info_bitfinex2(key, secrete) 
    api_bitfinex.balance()