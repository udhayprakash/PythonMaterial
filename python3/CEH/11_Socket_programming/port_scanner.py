#!/usr/bin/python
import sys
import time
from datetime import datetime
from socket import *

host = ''
max_port = 5000
min_port = 1


def scan_host(host, port, r_code=1):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex((host, port))

        if code == 0:
            r_code = code
        s.close()
    except Exception as ex:
        pass


try:
    host = raw_input('[*] Enter Target host address:')
except KeyboardInterrupt  as ex:
    print
    '\n\n[*] User initiated an interrupt'
    print
    '[*] Application Shutting down'
    sys.exit(1)

hostip = gethostbyname(host)
print
'\n[*] Host:%s IP:%s ' % (host, hostip)
print
'[*] Scanning started At %s ...\n' % (time.strftime('%H:%M:%S'))
start_time = datetime.now()

for port in range(min_port, max_port):
    try:
        response = scan_host(host, port)

        if response == 0:
            print
            '[*] Port %d: open' % (port)
    except Exception as e:
        pass

stop_time = datetime.now()
total_time_duration = stop_time - start_time
print
'\n[*] Scanning finished at %s ...' % (time.strftime('%H:%M:%S'))
print
'[*] Scanning Duration %s ...' % (total_time_duration)
