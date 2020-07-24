#!/usr/bin/python
"""
Purpose: To download a web page 

    To understand the url: https://dfir.blog/unfurl/
"""

import  urllib.request

# url = 'https://developer.yahoo.com/'
# url = 'https://google.com/'
url = 'https://rediff.com/'

url_handler = urllib.request.urlopen(url)
content = url_handler.read()

# print(type(content))

with open('rediff.html', 'wb') as f:
    f.write(content)
    f.close()