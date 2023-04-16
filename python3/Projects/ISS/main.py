#!/usr/bin/python
"""
Purpose:
"""
import argparse
from datetime import datetime

import requests


class ISS(object):
    def __init__(self):
        self.base_url = "http://api.open-notify.org"

    def get_response_data(self, endpoint, _params=None):
        response = requests.get(self.base_url + endpoint, params=_params, timeout=5)
        if response.headers["Content-Type"] == "application/json":
            response_content = response.json()
            return response_content

    def get_iss_location(self):
        response_data = self.get_response_data("/iss-now.json")
        latitude = response_data["iss_position"]["latitude"]
        longitude = response_data["iss_position"]["longitude"]
        response_str = "The ISS current location at {} is ({}, {})"
        current_time = datetime.now()
        return response_str.format(current_time, latitude, longitude)

    def get_iss_passage_info(self, latitude, longitude):
        """
        *   pass
           *   print the passing details of the ISS for a given location
           *   Example: “The ISS will be overhead {LAT, LONG} at {time} for {duration}”
        """
        params = {"lat": latitude, "lon": longitude}  # -15.3850° N, 54.4867° E
        response_data = self.get_response_data("/iss-pass.json", params)
        if response_data["message"] == "failure":
            return response_data["reason"]

        response_str = ""
        for each_pass in response_data["response"]:
            duration = each_pass["duration"]
            risetime = each_pass["risetime"]
            risetime = datetime.fromtimestamp(risetime)
            response_str += f"\nThe ISS will be overhead {latitude}, {longitude} at {risetime} for {duration} ms"
        return response_str.strip()

    def get_astronauts_info(self):
        """To get the Astronomers living in ISS now"""
        response_data = self.get_response_data("/astros.json")
        astros = [each["name"] for each in response_data["people"]]
        craft = response_data["people"][0]["craft"]
        return f'There are {len(astros)} people aboard the {craft}. They are {",".join(astros)}'


def get_args():
    parser = argparse.ArgumentParser(
        description="Details of International Space Station",
        epilog="""-----Please follow help doc ----
        -	loc
            -	print the current location of the ISS
            -	Example: “The ISS current location at {time} is {LAT, LONG}”
        -	pass
            -	print the passing details of the ISS for a given location
            -	Example: “The ISS will be overhead {LAT, LONG} at {time} for {duration}”
        -	people
            -	for each craft print the details of those people that are currently in space
            -	Example: “There are {number} people aboard the {craft}. They are {name[0]}…{name[n]}”
        """,
    )
    parser.add_argument("-g", "--get", choices=("loc", "pass", "people"), required=True)
    args = parser.parse_args()
    return args.get


if __name__ == "__main__":
    iss_client = ISS()
    option = get_args()
    if option == "loc":
        print(iss_client.get_iss_location())
    elif option == "pass":
        lat = input("Enter the latitude :")
        long = input("Enter the longitude:")
        print(iss_client.get_iss_passage_info(lat, long))
    else:  # option == 'people':
        print(iss_client.get_astronauts_info())
