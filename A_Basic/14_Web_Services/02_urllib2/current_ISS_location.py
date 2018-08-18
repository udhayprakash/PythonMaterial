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
# print help(pprint)
print obj['timestamp'], 'is equal to ', datetime.fromtimestamp(obj['timestamp'])

# print obj['iss_position']['latitude'], obj['iss_position']['longitude']

print 'At {time}, ISS is at lat:{lat}, long:{long}'.format(
    time=datetime.fromtimestamp(obj['timestamp']),
    lat=obj['iss_position']['latitude'],
    long=obj['iss_position']['longitude']
)
# Example prints:
#   1364795862
#   -47.36999493 151.738540034
import requests
google_reverse_geocode_URL = 'http://maps.googleapis.com/maps/api/geocode/json?latlng={LATITUDE},{LONGITUDE}&sensor=false'

request_url = google_reverse_geocode_URL.format(LATITUDE=obj['iss_position']['latitude'],
                                                LONGITUDE=obj['iss_position']['longitude'])

google_response = requests.get(request_url)
print google_response