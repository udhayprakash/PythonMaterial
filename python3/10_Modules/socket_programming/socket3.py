#!/usr/bin/python

'''
The python socket library has utilities to deal with various IP address formats.
Let us use  two of them: inet_aton() and inet_ntoa()
'''

import socket
from binascii import hexlify

def convertIp4Address():
    for ipAddr in ['127.0.0.1', '192.168.0.1']:
        packedIpAddress  = socket.inet_aton(ipAddr)
        unpackedIpAddress = socket.inet_ntoa(packedIpAddress)
        print "IP Address: %s => Packed : %s, Unpacked: %s"\
        %(ipAddr, hexlify(packedIpAddress), unpackedIpAddress)

if __name__ == '__main__':
    convertIp4Address()