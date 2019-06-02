#!/usr/bin/python

import socket

def convertInteger():
    data = 1234
    # 32-bit
    print "Original: %s => Long host byte order:%s, Network byte order: %s"\
    %(data, socket.ntohl(data), socket.htonl(data))
    # 64-bit
    print "Original: %s => short host byte order:%s, Network byte order: %s"\
    %(data, socket.ntohs(data), socket.htons(data))

if __name__ == '__main__':
    convertInteger()