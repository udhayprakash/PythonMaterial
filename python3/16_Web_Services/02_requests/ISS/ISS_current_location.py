#!/usr/bin/python3
"""
Purpose: 
  *   loc
     *   print the current location of the ISS
     *   Example: “The ISS current location at {time} is {LAT, LONG}”

"""
import requests
import sys
from datetime import datetime 
from pprint import pprint 

URL = 'http://api.open-notify.org/iss-now.json'

response = requests.get(URL)
print(response.status_code)
print(response.ok)
print(response.reason)
print(response.url)
# print(response.text)
# import json
# print(json.loads(response.text))
print(response.json())

if response.status_code != 200:
    print(response.text)
    sys.exit(1)

response_data = response.json()
pprint(response_data)

iss_latitude = response_data.get('iss_position', {}).get('latitude')
iss_longitude = response_data.get('iss_position', {}).get('longitude')

timestamp_raw = response_data.get('timestamp')
timestamp = datetime.fromtimestamp(timestamp_raw)

print(f'The ISS current location at {timestamp} is {iss_latitude, iss_longitude}')