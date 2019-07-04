#!/usr/bin/python

import sys
import socket
import argparse

def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action = 'store', dest='host', required = False)
    parser.add_argument('--port', action = 'store', dest= 'port', type = int, required = False)
    parser.add_argument('--file', action = 'store', dest = 'file', required = False)

    givenArgs = parser.parse_args()
    host = givenArgs.host
    port = givenArgs.port
    filename = givenArgs.file

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print("Error creating socket:%s"%e)
        sys.exit(1)

    try:
        s.connect((host, port))
    except socket.gaierror, e:
        print("Address-related error connecting to server: %s"%e)
        sys.exit(1)
    except socket.error, e:
        print("connection error: %s"%e)
        sys.exit(1)

    try:
        s.sendall("GET %s HTTP/1.0\r\n\\r\n"%filename)
    except socket.error, e:
        print("Error sending data: %s"%e)
        sys.exit(1)

    while 1:
        try:
            buf = s.recv(2048)
        except socket.error, e:
            print("Error receivig data: %s"%e)
            sys.exit(1)

        if not len(buf):
            break

        # Write the received data
        sys.stdout.write(buf)

if __name__ == '__main__':
    main()