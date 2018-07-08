from pprint import pprint

import requests

URL = 'https://api.jikan.moe/'
response = requests.get(URL)

data = response.json()
# print(data)
pprint(data)
