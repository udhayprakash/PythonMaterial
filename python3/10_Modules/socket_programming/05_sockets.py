#!/usr/bin/python

import socket

def convertInteger():
    data = 1234
    # 32-bit
    print(f'''Original: {data} 
            => Long host byte order:{socket.ntohl(data)}, 
            Network byte order     : {socket.htonl(data)}''')
    # 64-bit
    print(f'''Original: {data} 
            => short host byte order:{socket.ntohs(data)}, 
            Network byte order      : {socket.htons(data)}''')

if __name__ == '__main__':
    convertInteger()