#!/usr/bin/python
import socket,sys

# taking port from first argument

if len(sys.argv) != 3:
  print '''
          ./sys.argv[0] <hostname> <port no>
                  '''
  sys.exit()
else:
  host = str(sys.argv[1])
  port = int(sys.argv[2])



# creating a socket

try:
  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,error:
  print 'Failed to create a socket. Error Code: ' + str(error[0]) + ' , Error message :' + str(error[1])
  sys.exit()

print 'socket created'

#host = 'localhost'

try:
  remote_ip = socket.gethostbyname( host )
except:
  print 'Hostname could not be resolved.exiting'
  sys.exit()

print 'Ip address of ' + host + ' is ' + remote_ip

print "connecting to the server \n"

s.connect((remote_ip,port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip + ' on port ' + str(port)
  
