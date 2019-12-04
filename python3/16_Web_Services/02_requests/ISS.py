#!/usr/bin/python
"""
Purpose:
    http://api.open-notify.org/iss-now.json
"""
import requests
import json
from datetime import datetime
class ISSClient:
    def iss_now(self):
        response = requests.get('http://api.open-notify.org/iss-now.json')
        # print(type(response.text), response.text)
        response_data = json.loads(response.text)
        # print(type(response_data), response_data)
        if response_data['message'] != 'success':
            print(response_data['message'])
        else:
            iss_pos = response_data['iss_position']
            _lat = iss_pos.get('latitude')
            _lon = iss_pos.get('longitude')

            timestamp = response_data['timestamp']
            timestamp = datetime.utcfromtimestamp(timestamp)

            print(f'ISS is present at {_lat, _lon} at {timestamp}')

if __name__ == '__main__':
    iss = ISSClient()
    iss.iss_now()