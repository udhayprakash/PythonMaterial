#!/usr/bin/python
"""
Purpose: To get the http response status codes

    https://http.cat/[status_code]

            Http response status
                1xx     - Informational
                2xx     - success
                3xx     - redirect
                4xx     - client side
                5xx     - server side
"""
import ctypes
import os
from pprint import pp

import requests

URL = "https://http.cat/{HTTP_CODE}.jpg"
# url = "https://http.cat/100.jpg"


def get_status_images(_foldername):
    for each_code in range(100, 600):
        url = URL.format(HTTP_CODE=each_code)
        # print(url)

        response = requests.get(url)
        # pp(dict(response.headers))
        if (
            response.status_code == 200
            and response.headers["Content-Type"] == "image/jpeg"
        ):
            print(f"{response.url         =}")
            # print(response.content)
            file_path = os.path.join(_foldername, f"{each_code}.jpg")
            with open(file_path, "wb") as f:
                f.write(response.content)

            change_desktop_background(file_path)


def create_folder(foldername):
    # if not os.path.exists(foldername):
    #     os.makedir(foldername)

    os.makedirs(foldername, exist_ok=True)


def change_desktop_background(image_path):
    """To change the desktop background with that image"""
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)


if __name__ == "__main__":
    create_folder("http_status_cats")
    get_status_images("http_status_cats")
