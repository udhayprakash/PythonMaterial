#!/usr/bin/python

'''
The python socket library has utilities to deal with various IP address formats.
Let us use  two of them: inet_aton() and inet_ntoa()
'''

import socket
from binascii import hexlify

# convertIp4Address
for ipAddr in ('127.0.0.1', '192.168.47.1'):
    packedIpAddress = socket.inet_aton(ipAddr)
    unpackedIpAddress = socket.inet_ntoa(packedIpAddress)
    print(f''' 
   IP Address:{ipAddr}
      => Packed   : {hexlify(packedIpAddress).decode('utf-8')}
      => UnPacked : {unpackedIpAddress}
   ''')
