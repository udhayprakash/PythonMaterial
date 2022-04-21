#!/usr/bin/python
"""
Purpose: Get IP address
    http://httpbin.org/ip
"""
import requests
from pprint import pprint

response = requests.get("http://httpbin.org/ip")
print(f"{response.status_code =}")
print(f"{response.url         =}")

# pprint(dict(response.headers))

if response.headers["Content-Type"] == "application/json":
    response_data = response.json()
    # pprint(response_data)
    print(f'Your public IP address is {response_data["origin"]}')
