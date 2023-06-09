#!/usr/bin/python
"""
Purpose: Get my Public IP address
"""
import urllib.request

connection = urllib.request.urlopen("http://checkip.dyndns.org")

print(
    f"""
    {connection.url         = }
    {connection.geturl()    = }

    {connection.status      = }
    {connection.code        = }
    {connection.getcode()   = }

    {connection.reason      = }
    {connection.msg         = }

    {connection.version     = }
    {connection.length      = }

    {connection.readable()  = }
    {connection.writable()  = }
    {connection.seekable()  = }

    {connection.debuglevel  = }
    {connection.chunked     = }
    {connection.chunk_left  = }

    {connection.fileno()    = }

    {connection.will_close  = }
    {connection.closed      = }
    {connection.close()     = }
    {connection.isclosed()  = }

    {connection.getheader('Content-Type') = }
"""
)

for header_name, Value in connection.getheaders():
    print(f"{header_name:15}: {Value}")
