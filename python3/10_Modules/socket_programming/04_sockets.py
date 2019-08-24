#!/usr/bin/python

import socket

# findServiceName
protocol_name = 'udp'  #'tcp'
for port in range(10, 5000):
    try:
        service_name = socket.getservbyport(port, protocol_name)
        print(f'''Port:{port} => service name:{service_name}''') 
    except: 
        pass
    

