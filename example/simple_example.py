import bitfinex

# Initialize V1 API
apiV1 = bitfinex.bitfinex_v1.api_v1()

# Get the names of all pairs
pairs = apiV1.symbols()

# Initialize V2 API
apiV2 = bitfinex.bitfinex_v2.api_v2()

# Get ticker data for first pair
ticker = apiV2.ticker(pairs[0])

# Print the results
print('\nFound {} currency pairs.\n'
      'Ticker data for first pair ({}):\n'
      '{}'.format(len(pairs), pairs[0], ticker))
