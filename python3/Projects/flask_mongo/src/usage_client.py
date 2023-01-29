#!/usr/bin/python3
import requests

# response = requests.get('http://127.0.0.1:5000/')
# print(response.json())

response = requests.get(
    "http://127.0.0.1:5000/users/5f481bcafcedab42c8652d73", timeout=5
)
print(response.json())
