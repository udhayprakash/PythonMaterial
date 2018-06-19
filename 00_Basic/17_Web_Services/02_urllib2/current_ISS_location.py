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
2XX - success
3XX - redirecting 
4XX - client side errors
5XX - server side issues
"""
import json
import urllib2

req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)
obj = json.loads(response.read())

print obj['timestamp']
print obj['iss_position']['latitude'], obj['iss_position']['latitude']

# Example prints:
#   1364795862
#   -47.36999493 151.738540034
