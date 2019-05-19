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
import urllib.request

URL = 'https://http.cat/200'
req = urllib.request.Request(URL)
# print dir(req)

print('req.get_header', req.get_header)

response = urllib.request.urlopen(req)
print()
print('response.getcode()', response.getcode())
# print response.readline()  # image 
# print dir(response)
print(response.headers)