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

"""
import urllib2
import json

req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)

obj = json.loads(response.read())

print obj['timestamp']
print obj['iss_position']['latitude'], obj['iss_position']['latitude']

# Example prints:
#   1364795862
#   -47.36999493 151.738540034