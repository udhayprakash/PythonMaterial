#!/usr/bin/python
"""
Purpose: To get the current location of ISS. 

API 
    URL: http://api.open-notify.org/iss-now.json
    RESPONSE:
    {
        "message": "success", 
        "timestamp": UNIX_TIME_STAMP, 
        "iss_position": {
            "latitude": CURRENT_LATITUDE, 
            "longitude": CURRENT_LONGITUDE
        }
    }

http response codes 
----------------------
2XX - success
3XX - redirecting 
4XX - client side errors
5XX - server side issues
"""
import json
import urllib2
from pprint import pprint
from datetime import datetime

req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)

obj = json.loads(response.read())

# print 'obj', obj
pprint(obj, indent=2, depth=4)
# # print help(pprint)
print obj['timestamp'], 'is equal to ', datetime.fromtimestamp(obj['timestamp'])

print obj['iss_position']['latitude'], obj['iss_position']['longitude']

print 'At {TIME}, ISS is at lat:{LAT}, long:{LONG}'.format(
                            TIME=datetime.fromtimestamp(obj['timestamp']),
                            LAT=obj['iss_position']['latitude'],
                            LONG=obj['iss_position']['longitude']
                        )
# Example prints:
#   1364795862
#   -47.36999493 151.738540034
import requests
from pprint import pprint

# google_reverse_geocode_URL = 'http://maps.googleapis.com/maps/api/geocode/json?latlng={LATITUDE},{LONGITUDE}&sensor=false'

# request_url = google_reverse_geocode_URL.format(LATITUDE=obj['iss_position']['latitude'],
#                                                 LONGITUDE=obj['iss_position']['longitude'])

# google_response = requests.get(request_url)
# print(google_response.json())


# #####################################

def get_address_for_given_coordinates(latitude, longitude):
    REVERSE_SEARCH_URL = 'https://nominatim.openstreetmap.org/reverse?'
    payload = {'lat': latitude,
               'lon': longitude,
               'format': 'json',
               'zoom': 18,
               'addressdetails': 1}

    response = requests.get(REVERSE_SEARCH_URL, params=payload).json()
    # pprint(response)
    if response.get('error'):
        print(response.get('error'))
        return

    result_string = u'''
            ====Corresponding Address=====
            VILLAGE: {village}
            STATE DISTRICT: {state_district}
            STATE:{state}
            ROAD: {road}
            POSTCODE: {postcode}
            FUEL:{fuel}
            COUNTRY CODE: {country_code}
            COUNTRY: {country}'''.format(
                village=response.get('address', {}).get('village', ''),
                state_district=response.get('address', {}).get('state_district', ''),
                state=response.get('address', {}).get('state', ''),
                road=response.get('address', {}).get('road', ''),
                postcode=response.get('address', {}).get('postcode', ''),
                fuel=response.get('address', {}).get('fuel', ''),
                country_code=response.get('address', {}).get('country_code', ''),
                country=response.get('address', {}).get('country', ''))
    print(result_string)


get_address_for_given_coordinates(
    obj['iss_position']['latitude'],
    obj['iss_position']['longitude']
)
