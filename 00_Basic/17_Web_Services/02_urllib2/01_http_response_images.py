#!/usr/bin/python
"""
https://http.cat/[status_code]
"""
import json
import urllib2

URL = 'https://http.cat/200'
req = urllib2.Request(URL)
response = urllib2.urlopen(req)

print response.getcode
print response.readline()
print dir(response)