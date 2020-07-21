#!/usr/bin/python

'''
Network Time Protocol(NTP) - ntplib
    Used to synchronize your machine time with one of the Internet time servers

    pip install ntplib
'''

try:
    import ntplib
except ImportError as ie:
    print(ie)
    print("Trying to install the module")
    from os import system

    if not system('pip install ntplib --user'):
        print("Unable to install module")
        from sys import exit

        exit(1)

from time import ctime


def printTime():
    ntpClient = ntplib.NTPClient()
    response = ntpClient.request('pool.ntp.org')
    print(ctime(response.tx_time))


if __name__ == '__main__':
    printTime()
