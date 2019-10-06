#!/usr/bin/python
# third.py
import socket
import sys

# host = 'localhost'
host = raw_input("Enter the host name to connect(ex: www.google.com) : ")
port = int(raw_input("Enter the port to connect (ex: 80) : "))

# creating a socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, error:
    print
    'Failed to create a socket. Error Code: ' + str(error[0]) + ' , Error message :' + str(error[1])
    sys.exit()

print
'socket created'

try:
    remote_ip = socket.gethostbyname(host)
except:
    print
    'Hostname could not be resolved.exiting'
    sys.exit()

print
'Ip address of ' + host + ' is ' + remote_ip

print
"connecting to the server \n"
try:
    s.connect((remote_ip, port))
except socket.error, error:
    print
    'Failed to create a socket. Error Code: ' + str(error[0]) + ' , Error message :' + str(error[1])
    sys.exit()
print
'Socket Connected to ' + host + ' on ip ' + remote_ip + ' on port ' + str(port)
