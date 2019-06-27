#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Purpose:   Testing https://www.metaweather.com/api/

pip install requests

http request methods
    GET
    POST
    PUT
    UPDATE
    DELETE
    CREATE

"""

from pprint import pprint
import json
import requests
# pip install -U requests


def get_data_n_write_to_file(URL):
    response = requests.get(URL)
    print(response.status_code)
    if 200 <= response.status_code < 300:
        # storing in a json file
        json_response = response.json()
        with open('result.json', 'w') as f:
            json.dump(json_response, f)
            f.close()


URL = 'https://www.metaweather.com/api/location/search1/?query=new%20york'
get_data_n_write_to_file(URL)

URL = 'https://www.metaweather.com/api/location/search/?query=san'
get_data_n_write_to_file(URL)



# def location_search(query):
#     try:
#         response = requests.get(r'https://www.metaweather.com//api/location/search/?query=' + query)
#         if response.status_code == 200:
#             pprint(response.json())
#             for res in response.json():
#                 print res['title'] + ' is a ' + res['location_type'] + ' located at ' + res['latt_long']
#         else:
#             print 'Unsuccessful call. Response code is ', response.status_code
#         print
#     except Exception as ex:
#         print 'Unable to execute call. Error is', ex


# location_search('Hyderabad')
# location_search('India')
# location_search('Anakapalle')  # mid-size town in India
# location_search('san')
# location_search('Alabama')
# location_search('canada')
# location_search('vancouver')
