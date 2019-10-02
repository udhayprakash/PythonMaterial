# https://realpython.com/python-bitcoin-ifttt/

import requests
from pprint import pprint

bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
response = requests.get(bitcoin_api_url)
response_json = response.json()
print(type(response_json))  # The API returns a list

# Bitcoin data is the first element of the list
pprint(response_json[0])
