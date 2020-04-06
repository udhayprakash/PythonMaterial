#!/usr/bin/python3
"""
Purpose: 
 *   pass
     *   print the passing details of the ISS for a given location
     *   Example: “The ISS will be overhead {LAT, LONG} at {time} for {duration}”

"""
import sys
from datetime import datetime

import requests

URL = 'http://api.open-notify.org/iss-pass.json'

choosen_lat = input('Enter Latitude:')
choosen_long = input('Enter Longitude:')
response = requests.get(URL, params={'lat': choosen_lat, 'lon': choosen_long})

# if response.status_code != 200:
#     print(response.text)
#     sys.exit(1)

print('response.url', response.url)
response_data = response.json()

from pprint import pprint

pprint(response_data)

if response_data.get('message') != 'success':
    print(response_data.get('reason'))
    sys.exit(1)

for each in response_data.get('response'):
    duration = each.get('duration')
    timestamp_raw = each.get('risetime')
    timestamp = datetime.fromtimestamp(timestamp_raw)
    print(f'The ISS was overhead {choosen_lat, choosen_long} at {timestamp} for {duration}')
