#!/usr/bin/python
"""
Purpose: Get IP address
    http://httpbin.org/user-agent
"""
import requests
from pprint import pprint

response = requests.get('http://httpbin.org/user-agent')
print(f'{response.status_code =}')
print(f'{response.url         =}')

# pprint(dict(response.headers))

if response.headers['Content-Type'] == 'application/json':
    response_data = response.json()
    print(f'You are hitting this API with {response_data["user-agent"]}')


# Method 2
import urllib.request
import json
url_handler = urllib.request.urlopen('http://httpbin.org/user-agent')

response = url_handler.read()
response_data = json.loads(response)
print(f'You are hitting this API with {response_data["user-agent"]}')
