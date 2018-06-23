from pprint import pprint
from xml.etree import ElementTree

import requests

URL = 'https://api.jikan.moe/'
response = requests.get(URL)

data = response.json()
# print(data)
pprint(data)
