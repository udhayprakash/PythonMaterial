#!/usr/bin/python

import socket
import sys
from thread import *

HOST = 'localhost'
PORT = 9865
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print
    'Bind Failed. Error code : ' + str(msg[0]) + ' message ' + msg[1]
    sys.exit()

print
'Socket binding completed'

s.listen(10)
print
'socket now listening'


def clientthread(conn):
    conn.send('welcome to the server. Type something and hit enter \n')

    while True:
        data = conn.recv(1024)
        reply = 'OK .. ' + data
        if not data:
            break
        conn.sendall(reply)

    conn.close()


while 1:
    conn, addr = s.accept()
    print
    "connected with" + addr[0] + ':' + str(addr[1])
    start_new_thread(clientthread, (conn,))

s.close()
