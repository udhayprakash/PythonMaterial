#!/usr/bin/python
# fourth.py
import socket
import sys

HOST = 'localhost'
PORT = 8888
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

conn, addr = s.accept()
print
"connected with" + addr[0] + ':' + str(addr[1])

data = conn.recv(1024)
conn.sendall(data)

conn.close()
s.close()
