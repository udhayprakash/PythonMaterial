#!/usr/bin/python3
"""
Purpose: 
 *   people
     *   for each craft print the details of those people that are currently in space
     *   Example: “There are {number} people aboard the {craft}. They are {name[0]}…{name[n]}”

"""
import requests
import sys
from datetime import datetime 

URL = 'http://api.open-notify.org/astros.json'

response = requests.get(URL)

if response.status_code != 200:
    print(response.text)
    sys.exit(1)


response_data = response.json()

if response_data.get('message') != 'success':
    print(response_data.get('reason'))
    sys.exit(1)


from pprint import pprint 
pprint(response_data)

number = response_data.get('number')   
craft = response_data.get('people')[0].get('craft')

people_names = []
for each in response_data.get('people'):
    people_names.append(each.get('name'))

people_names = ','.join(people_names)
print(f'There are {number} people aboard the {craft}. They are {people_names}')



