#!/usr/bin/python
"""
Purpose: Google search
pip install -U requests --user
"""
import requests

response = requests.get('https://www.google.com/search?q=python+programming&oq=python+programming&aqs=chrome..69i57j69i65l3j69i61j69i60.6334j0j7&sourceid=chrome&ie=UTF-8')
print(response)

print(dir(response))

print(f'response.url        :{response.url}')
print(f'response.ok         :{response.ok}')
print(f'response.status_code:{response.status_code}')
print(f'response.reason     :{response.reason}')
print(response.text)

with open('google_search.html', 'w') as f:
    f.write(response.text)
    f.close()
