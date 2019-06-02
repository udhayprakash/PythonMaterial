#sockets

import socket

hostName = socket.gethostname()
print "Host name: %s"%hostName

print "IP address: %s"%socket.gethostbyname(hostName)