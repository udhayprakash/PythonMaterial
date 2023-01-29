#!/usr/bin/python

import socket

host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

print(
    f"""
Host name : {host_name}
IP address: {ip_address}"""
)

# port address = mac address == private ip address  ==== ISP (Public IP Adress) ==== Internet

# internet address      -  ip adrress
# device address        - MAC address
# applciation address   - port address
