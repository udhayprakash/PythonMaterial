#!/usr/bin/python
"""
Purpose: open street map API usage
https://wiki.openstreetmap.org/wiki/Nominatim#Example
"""

import requests


def get_address_for_given_coordinates(latitude, longitude):
    REVERSE_SEARCH_URL = "https://nominatim.openstreetmap.org/reverse?"
    payload = {
        "lat": latitude,
        "lon": longitude,
        "format": "json",
        "zoom": 18,
        "addressdetails": 1,
    }

    response = requests.get(REVERSE_SEARCH_URL, params=payload).json()
    # pprint(response)
    if response.get("error"):
        print(response.get("error"))
        return

    result_string = """
    ====Corresponding Address=====
    VILLAGE: {village}
    STATE DISTRICT: {state_district}
    STATE:{state}
    ROAD: {road}
    POSTCODE: {postcode}
    FUEL:{fuel}
    COUNTRY CODE: {country_code}
    COUNTRY: {country}""".format(
        village=response.get("address", {}).get("village", ""),
        state_district=response.get("address", {}).get("state_district", ""),
        state=response.get("address", {}).get("state", ""),
        road=response.get("address", {}).get("road", ""),
        postcode=response.get("address", {}).get("postcode", ""),
        fuel=response.get("address", {}).get("fuel", ""),
        country_code=response.get("address", {}).get("country_code", ""),
        country=response.get("address", {}).get("country", ""),
    )
    print(result_string)


if __name__ == "__main__":
    search_latitude, search_longitude = (
        input("Enter GPS coorinate (latitude, longitude):").replace(" ", "").split(",")
    )
    get_address_for_given_coordinates(search_latitude, search_longitude)
