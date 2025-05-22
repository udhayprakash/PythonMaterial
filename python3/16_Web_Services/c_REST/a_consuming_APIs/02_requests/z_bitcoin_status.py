# https://realpython.com/python-bitcoin-ifttt/

from pprint import pprint
from security import safe_requests

bitcoin_api_url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
response = safe_requests.get(bitcoin_api_url, timeout=60)
response_json = response.json()
print(type(response_json))  # The API returns a list

# Bitcoin data is the first element of the list
pprint(response_json[0])
