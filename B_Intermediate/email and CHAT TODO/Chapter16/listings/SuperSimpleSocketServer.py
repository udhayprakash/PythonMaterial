#!/usr/bin/python
import socket
import sys

if len(sys.argv) < 3:
    print 'Usage: %s [hostname] [port number]' % sys.argv[0]
    sys.exit(1)

hostname = sys.argv[1]
port = int(sys.argv[2])

#Set up a standard Internet socket. The setsockopt call lets this
#server use the given port even if it was recently used by another
#server (for instance, an earlier incarnation of
#SuperSimpleSocketServer).
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Bind the socket to a port, and bid it listen for connections.
sock.bind((hostname, port))
sock.listen(1)
print "Waiting for a request."

#Handle a single request.
request, clientAddress = sock.accept()
print "Received request from", clientAddress
request.send('-=SuperSimpleSocketServer 3000=-\n')
request.send('Go away!\n')
request.shutdown(2) #Stop the client from reading or writing anything.
print "Have handled request, stopping server."
sock.close()
