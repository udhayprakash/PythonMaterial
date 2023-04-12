#!/usr/bin/python3
"""
Purpose: Sending Secue requests

    pip install certifi

"""
import certifi
import urllib3

http = urllib3.PoolManager(ca_certs=certifi.where())
response = http.request("GET", "https://httpbin.org/get")

print(response.status)
