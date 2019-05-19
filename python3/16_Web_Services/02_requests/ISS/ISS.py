#!/usr/bin/python
"""
 *   loc
     *   print the current location of the ISS
     *   Example: “The ISS current location at {time} is {LAT, LONG}”
  *   pass
     *   print the passing details of the ISS for a given location
     *   Example: “The ISS will be overhead {LAT, LONG} at {time} for {duration}”
  *   people
     *   for each craft print the details of those people that are currently in space
     *   Example: “There are {number} people aboard the {craft}. They are {name[0]}…{name[n]}”
"""
import requests
import sys
from datetime import datetime 

def get_response(_url, _request_params = None):
    response = requests.get(_url, params=_request_params)
    if response.status_code != 200:
        print(response.text)
        sys.exit(1)
    # print('response.url', response.url)
    return response.json()

def get_iss_location_info():
    URL = 'http://api.open-notify.org/iss-now.json'
    response_data = get_response(URL)

    iss_latitude = response_data.get('iss_position', {}).get('latitude')
    iss_longitude = response_data.get('iss_position', {}).get('longitude')

    timestamp_raw = response_data.get('timestamp')
    timestamp = datetime.fromtimestamp(timestamp_raw)

    print(f'The ISS current location at {timestamp} is {iss_latitude, iss_longitude}')


def get_iss_passage_info():
    URL = 'http://api.open-notify.org/iss-pass.json'

    choosen_lat = input('Enter Latitude:')
    choosen_long = input('Enter Longitude:')

    request_query_params = {'lat':choosen_lat, 'lon':choosen_long}
    response_data = get_response(URL, request_query_params)

    if response_data.get('message') != 'success':
        print(response_data.get('reason'))
        sys.exit(1)

    for each in response_data.get('response'):
        duration = each.get('duration')
        timestamp_raw = each.get('risetime')
        timestamp = datetime.fromtimestamp(timestamp_raw)
        print(f'The ISS will be overhead {choosen_lat, choosen_long} at {timestamp} for {duration}')
        
        
def get_iss_astros_info():
    URL = 'http://api.open-notify.org/astros.json'
    response = requests.get(URL)
    response_data = response.json()

    if response_data.get('message') != 'success':
        print(response_data.get('reason'))
        sys.exit(1)

    number = response_data.get('number')   
    craft = response_data.get('people')[0].get('craft')

    people_names = []
    for each in response_data.get('people'):
        people_names.append(each.get('name'))

    people_names = ','.join(people_names)
    print(f'There are {number} people aboard the {craft}. They are {people_names}')


if __name__ == '__main__':   
    while True:
        entered_choice = input('\nEnter a choice: loc, pass or people\n*\t')

        if entered_choice == 'loc':
            get_iss_location_info()
        elif entered_choice =='pass':
            get_iss_passage_info()
        elif entered_choice == 'people':
            get_iss_astros_info()

        if input('\nEnter n or N to stop;any other key to continue:').lower() == 'n':
            break