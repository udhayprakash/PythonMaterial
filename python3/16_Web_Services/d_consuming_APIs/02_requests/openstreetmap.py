#!/usr/bin/python
"""
Purpose: open street map API usage
https://wiki.openstreetmap.org/wiki/Nominatim#Example
"""

import requests


def get_location_coordinates(search_string):
    SEARCH_URL = "https://nominatim.openstreetmap.org/search?"
    payload = {"q": search_string, "format": "json", "polygon": 1, "addressdetails": 1}

    response = requests.get(SEARCH_URL, params=payload).json()
    # pprint(response)
    for each in response:
        result_string = """====Search Result=====\n{DISPLAY_NAME}
                           latitude: {LATITUDE}
                           longitude:{LONGITUDE}""".format(
            DISPLAY_NAME=each.get("display_name"),
            LATITUDE=each.get("lat"),
            LONGITUDE=each.get("lon"),
        )
        print(result_string)


if __name__ == "__main__":
    searching_string = input("Enter an address:")
    get_location_coordinates(searching_string)
