#!/usr/bin/python
import socket
import sys

# creating a socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print
    'Failed to create a socket. Error Code: ' + str(error[0]) + ' , Error message :' + str(error[1])
    sys.exit(1)

print
'socket created'

host = 'google.com'  # 'server.myDomain.com'   #'localhost'
port = 80

try:
    remoteIp = socket.gethostbyname(host)
except:
    print
    'Hostname could not be resolved.exiting'
    sys.exit()

print
'Ip address of ' + host + ' is ' + remoteIp

print
"connecting to the server \n"

try:
    s.connect((remoteIp, port))
except socket.error, error:
    print
    'Failed to create a socket. Error Code: ' + str(error[0]) + ' , Error message :' + str(error[1])
    sys.exit()

print
'Socket Connected to ' + host + ' on ip ' + remoteIp
