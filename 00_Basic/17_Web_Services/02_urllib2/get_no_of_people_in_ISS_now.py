#!/usr/bin/python
"""
Purpose: To get the No. of people living in ISS now.

API 
    URL: http://api.open-notify.org/astros.json
    RESPONSE:
    {
        "message": "success",
        "number": NUMBER_OF_PEOPLE_IN_SPACE,
        "people": [
            {"name": NAME, "craft": SPACECRAFT_NAME},
            ...
        ]
    }

"""
import urllib2
import json

req = urllib2.Request("http://api.open-notify.org/astros.json")
response = urllib2.urlopen(req)

obj = json.loads(response.read())

print obj['message']
if obj['message'] == 'success':
    people_count = obj['number']
    print "Currently, total number of people living in ISS now are %d in number"%people_count
