#!/usr/bin/python
"""
https://http.cat/[status_code]

Http response status
    2xx     - success
    3xx     - redirect
    4xx     - client side
    5xx     - server side
"""
import ctypes
import os

import requests

# existing_images_in_cats_site  = xrange(100, 600)
existing_images_in_cats_site = (
    100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 408,
    409,
    410, 411, 412, 413, 414, 415, 416, 417, 418, 420, 421, 422, 423, 424, 425, 426, 429, 431, 444, 450, 451, 500, 502,
    503,
    504, 506, 507, 508, 509, 510, 511, 599)

for each_number in existing_images_in_cats_site:
    URL = 'https://http.cat/{HTTP_CODE}.jpg'.format(HTTP_CODE=each_number)
    response = requests.get(URL)
    print(URL)
    if response.status_code == 200 and response.headers['content-type'] == 'image/jpeg':
        dirname = 'http response code images'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        with open(dirname + os.sep + str(each_number) + '.jpg', 'wb') as g:
            g.write(response.content)
            g.close()

        # To change the desktop background with that image
        image = str(each_number) + '.jpg'
        image_path = os.path.join(dirname, image)
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
