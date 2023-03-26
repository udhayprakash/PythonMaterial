#!/usr/bin/python
"""
Purpose:
 *   pass
     *   print the passing details of the ISS for a given location
     *   Example: “The ISS will be overhead {LAT, LONG} at {time} for {duration}”

     http://api.open-notify.org/iss-pass.json?lat=23&lon=21
"""
from pprint import pp

import requests

URL = "http://api.open-notify.org/iss-pass.json"

latitude = input("Enter the latitude:")
longitude = input("Enter the longitude:")
# 17.3850° N, 78.4867° E

response = requests.get(URL, params={"lat": latitude, "lon": longitude})

print(f"{response.url         =}")
print(f"{response.status_code =}")
print(f"{response.reason      =}")

pp(response.headers)


# NOT FOUND
# THIS END POINT IS DISCONTINUED NOW
