#!/usr/bin/python
"""
Purpose: To get the details of a given IP Address

http://freegeoip.net/json/
"""
from pprint import pprint

import requests

URL = 'http://freegeoip.net/json/'

response = requests.get(URL)
geodata = response.json()

# print(geodata)
pprint(geodata)
