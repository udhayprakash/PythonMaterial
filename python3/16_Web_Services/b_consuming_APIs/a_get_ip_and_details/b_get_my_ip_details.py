#!/usr/bin/python
"""
Purpose: Getting IP details 

    GET https://ipapi.co/{format}/

"""
import urllib.request

def get_response(url):
    file_extension = url.split('/')[-1] or 'html'
    with urllib.request.urlopen(url) as url_handler:
        content = url_handler.read()
        with open('result.{}'.format(file_extension), 'wb') as f:
            f.write(content)
            f.close()

if __name__ == '__main__':
    get_response('https://ipapi.co/')
    get_response('https://ipapi.co/json')
    get_response('https://ipapi.co/yaml')
    get_response('https://ipapi.co/csv')
