#!/usr/bin/python
"""
Purpose: To get the Astronomers living in ISS now
    
    http://api.open-notify.org/astros.json
"""
import requests
from pprint import pprint

response = requests.get('http://api.open-notify.org/astros.json')
# print(f'{response.status_code =}')
# print(f'{response.url         =}')
# print(f'{response.reason      =}')
# print(f'{response.ok          =}')
# print(f'{response.is_redirect =}')
# print(f'{response.is_permanent_redirect =}')
# print(f'{response.elapsed    =}')

# pprint(dict(response.headers))

if response.headers['Content-Type'] == 'application/json':
    response_content = response.json()
    # pprint(response_content)
    number = response_content['number']

    astros = []
    for each in response_content['people']:
        astros.append(each['name'])

    craft = each['craft']

    print(f'''
        CRAFT               : {craft}
        No. Of ASTRONOMERS  : {number}
        Names of Astronomers: {astros}
    ''')