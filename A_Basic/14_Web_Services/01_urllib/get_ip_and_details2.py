import urllib

"""
https://ipapi.co/api/#location-of-a-specific-ip
"""
import os


def print_n_write_response(ip_address, output_format):
    url = 'https://ipapi.co/{ip}/{format}/'.format(ip=ip_address, format=output_format)

    connection = urllib.urlopen(url)
    data = connection.read()
    write_response_to_file(data, output_format)
    print data


def write_response_to_file(data, extension_name):
    dirname = os.path.splitext(os.path.relpath(__file__))[0]
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    with open(dirname + os.sep + 'response.' + extension_name, 'wb') as f:
        f.write(data)
        f.close()


print '-' * 20
print 'JSON response'
print_n_write_response('157.119.108.242', 'json')
print

print '-' * 20
print 'JSONP response'
print_n_write_response('157.119.108.242', 'jsonp')
print

print '-' * 20
print 'XML response'
print_n_write_response('157.119.108.242', 'xml')
print

print '-' * 20
print 'CSV response'
print_n_write_response('157.119.108.242', 'csv')
print

print '-' * 20
print 'YAML response'
print_n_write_response('157.119.108.242', 'yaml')
print
