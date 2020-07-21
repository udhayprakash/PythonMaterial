#!/usr/bin/python
"""
Purpose: Getting IP details 

    GET https://ipapi.co/{format}/

"""
import urllib.request

url = 'https://ipapi.co/'
with urllib.request.urlopen(url) as url_handler:
    content = url_handler.read()
    # print(type(content), content)
    with open('result.html', 'wb') as f:
        f.write(content.replace(b' ', b''))
        f.close()

url = 'https://ipapi.co/json'
with urllib.request.urlopen(url) as url_handler:
    content = url_handler.read()
    # print(type(content), content)
    with open('result.json', 'wb') as f:
        f.write(content)
        f.close()

url = 'https://ipapi.co/yaml'
with urllib.request.urlopen(url) as url_handler:
    content = url_handler.read()
    # print(type(content), content)
    with open('result.yaml', 'wb') as f:
        f.write(content)
        f.close()

url = 'https://ipapi.co/csv'
with urllib.request.urlopen(url) as url_handler:
    content = url_handler.read()
    # print(type(content), content)
    with open('result.csv', 'wb') as f:
        f.write(content)
        f.close()