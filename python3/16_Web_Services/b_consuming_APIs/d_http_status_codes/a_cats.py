#!/usr/bin/python
"""
Purpose: To get the http response status codes

    https://http.cat/[status_code]

            Http response status
                2xx     - success
                3xx     - redirect
                4xx     - client side
                5xx     - server side
"""
import os
import ctypes
import requests
from pprint import pprint

URL = "https://http.cat/{HTTP_CODE}.jpg"


# Create folder, if not exists
dirname = "https_status_images"
if not os.path.exists(dirname):
    os.mkdir(dirname)
os.chdir(dirname)
print(f"{os.getcwd() =}")

existing_images_in_cats_site = (
    100,
    101,
    200,
    201,
    202,
    204,
    206,
    207,
    300,
    301,
    302,
    303,
    304,
    305,
    307,
    400,
    401,
    402,
    403,
    404,
    405,
    406,
    408,
    409,
    410,
    411,
    412,
    413,
    414,
    415,
    416,
    417,
    418,
    420,
    421,
    422,
    423,
    424,
    425,
    426,
    429,
    431,
    444,
    450,
    451,
    500,
    502,
    503,
    504,
    506,
    507,
    508,
    509,
    510,
    511,
    599,
)

# for each_code in range(100, 600):
for each_code in existing_images_in_cats_site:
    response = requests.get(URL.format(HTTP_CODE=each_code))

    if response.status_code == 200 and response.headers["Content-Type"] == "image/jpeg":

        print(f"{response.url         =}")
        # pprint(dict(response.headers))
        with open(f"{each_code}.jpg", "wb") as f:
            f.write(response.content)
            f.close()

        # To change the desktop background with that image
        image = f"{each_code}.jpg"
        image_path = os.path.join(dirname, image)
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(
            SPI_SETDESKWALLPAPER, 0, image_path, 3
        )
