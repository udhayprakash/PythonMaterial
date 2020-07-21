#!/usr/bin/python
import socket, sys

# creating a socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print(f'Failed to create a socket. {repr(error)}')
    sys.exit()

print('socket created')

host = 'localhost'
port = 9999

try:
    remote_ip = socket.gethostbyname(host)
except:
    print('Hostname could not be resolved.exiting')
    sys.exit()

print('Ip address of ' + host + ' is ' + remote_ip)

print("connecting to the server \n")

s.connect((remote_ip, port))

print('Socket Connected to ' + host + ' on ip ' + remote_ip)
