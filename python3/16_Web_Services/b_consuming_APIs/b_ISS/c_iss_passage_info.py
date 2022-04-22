#!/usr/bin/python
"""
Purpose:
 *   pass
     *   print the passing details of the ISS for a given location
     *   Example: “The ISS will be overhead {LAT, LONG} at {time} for {duration}”

     http://api.open-notify.org/iss-pass.json?lat=23&lon=21
"""
from datetime import datetime
from pprint import pprint

import requests

URL = "http://api.open-notify.org/iss-pass.json"


latitude = input("Enter the latitude:")
longitude = input("Enter the longitude:")

response = requests.get(URL, params={"lat": latitude, "lon": longitude})

# 17.3850° N, 78.4867° E

print(f"{response.url         =}")
print(f"{response.status_code =}")
print(f"{response.reason      =}")

if response.headers["Content-Type"] == "application/json":
    response_content = response.json()
    # pprint(response_content)

    for each_pass in response_content["response"]:
        duration = each_pass["duration"]
        risetime = each_pass["risetime"]
        risetime = datetime.fromtimestamp(risetime)

        print(
            f"The ISS will be overhead {latitude}, {longitude} at {risetime} for {duration} ms"
        )
