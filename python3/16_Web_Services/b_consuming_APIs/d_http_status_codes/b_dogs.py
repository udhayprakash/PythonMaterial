#!/usr/bin/python
"""
https://httpstatusdogs.com/[status_code]

Http response status
    1xx     - Information
    2xx     - success
    3xx     - redirect
    4xx     - client side
    5xx     - server side
"""
import os

import requests
from a_cats import create_folder


def get_status_dogs(foldername):
    # existing_images_in_dogssite = range(100, 600)
    existing_images_in_dogs_site = (
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

    for each_status_code in existing_images_in_dogs_site:
        URL = f"https://httpstatusdogs.com/img/{each_status_code}.jpg"
        response = requests.get(URL)
        if (
            response.status_code == 200
            and response.headers["content-type"] == "image/jpeg"
        ):
            print(f"{URL =}")
            file_path = os.path.join(foldername, f"{each_status_code}.jpg")
            with open(file_path, "wb") as fh:
                fh.write(response.content)


if __name__ == "__main__":
    create_folder("http_status_dogs")
    get_status_dogs("http_status_dogs")
