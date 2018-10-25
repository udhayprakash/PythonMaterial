#!/usr/bin/python

"""
GET https://ipapi.co/{format}/
"""
import os
import urllib


def print_n_write_response(url):
    connection = urllib.urlopen(url)
    data = connection.read()
    write_response_to_file(data, url.split('/')[-1])
    print data


def write_response_to_file(data, extension_name):
    dirname = os.path.splitext(os.path.relpath(__file__))[0]
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    with open(dirname + os.sep + 'response.' + extension_name, 'wb') as f:
        f.write(data)
        f.close()


if __name__ == '__main__':
    print '-' * 20
    print 'JSON response'
    URL = 'https://ipapi.co/json'
    print_n_write_response(URL)
    print

    print '-' * 20
    print 'JSONP response'
    URL1 = 'https://ipapi.co/jsonp'
    print_n_write_response(URL1)
    print

    print '-' * 20
    print 'XML response'
    URL2 = 'https://ipapi.co/xml'
    print_n_write_response(URL2)
    print

    print '-' * 20
    print 'CSV response'
    URL3 = 'https://ipapi.co/csv'
    print_n_write_response(URL3)
    print

    print '-' * 20
    print 'YAML response'
    URL4 = 'https://ipapi.co/yaml'
    print_n_write_response(URL4)
    print
