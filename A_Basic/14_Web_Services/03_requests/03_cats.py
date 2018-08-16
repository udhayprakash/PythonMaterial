#!/usr/bin/python
"""
https://http.cat/[status_code]

Http response status
    2xx     - success
    3xx     - redirect
    4xx     - client side
    5xx     - server side
"""
import requests
import os

for each_number in xrange(100, 600):
    URL = 'https://http.cat/{HTTP_CODE}.jpg'.format(HTTP_CODE=each_number)
    response = requests.get(URL)
    print URL
    if response.status_code == 200 and response.headers['content-type'] == 'image/jpeg':
        dirname = 'http response code images'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        with open(dirname + os.sep + str(each_number) + '.jpg', 'wb') as g:
            g.write(response.content)
            g.close()
