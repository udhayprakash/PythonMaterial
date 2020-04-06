#!/usr/bin/python
"""
Purpose:
    https://http.cat/101.jpg
"""
from pprint import pprint

import requests

res = requests.get('https://http.cat/101.jpg')
print(f'res.status_code : {res.status_code}')
print(f'res.ok          : {res.ok}')
print(f'res.reason      : {res.reason}')
# print(f'res.text        :{res.text}')

print(f'res.content     : {res.content}')

print(f'res.headers     : ')
pprint(res.headers)
print(f"res.headers['Content-Type']: {res.headers['Content-Type']}")  # image/jpeg

with open('101.jpg', 'wb') as f:
    f.write(res.content)
    f.close()