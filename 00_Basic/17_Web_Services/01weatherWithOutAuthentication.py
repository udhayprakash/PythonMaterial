#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Purpose:   Testing https://www.metaweather.com/api/
"""

import requests
from pprint import pprint


def location_search(query):
    try:
        response = requests.get(r'https://www.metaweather.com//api/location/search/?query=' + query)
        if response.status_code == 200:
            # pprint(response.json())
            for res in response.json():
                print res['title'] + ' is a ' + res['location_type'] + ' located at ' + res['latt_long']
        else:
            print 'Unsuccessful call. Response code is ', response.status_code
        print
    except Exception as ex:
        print 'Unable to execute call. Error is', ex


location_search('Hyderabad')
location_search('India')
location_search('Anakapalle')  # mid-size town in India
location_search('san')
location_search('Alabama')
location_search('canada')
location_search('vancouver')
