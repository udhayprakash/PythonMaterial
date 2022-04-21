#!usr/bin/python

import socket


def testSocketTimeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'Default socket timeout:{s.gettimeout()}')
    s.settimeout(100)
    print(f'Current socket timeout:{s.gettimeout()}')


if __name__ == '__main__':
    testSocketTimeout()
