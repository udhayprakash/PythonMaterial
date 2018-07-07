#!/usr/bin/python
"""
https://http.cat/[status_code]

Http response status
    2xx     - success
    3xx     - redirect
    4xx     - client side
    5xx     - server side
"""
import json
import urllib2

URL = 'https://http.cat/200'
req = urllib2.Request(URL)
response = urllib2.urlopen(req)

print response.getcode
print response.readline()  # image 
print dir(response)