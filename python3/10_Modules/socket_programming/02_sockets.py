import socket

remote_host = 'www.python.org'
ip_address = socket.gethostbyname(remote_host)

try:
    print(f"IP address: {ip_address}")
except socket.error  as err_msg:
    print(f'{remote_host} : {err_msg}')

# DNS 
# 151.101.8.223 == 'www.python.org'
