#!/usr/bin/python 
"""
Purpose: importance and usage of argparse
"""

# Method 1: hard- coding
# user_name = 'udhay'
# password = 'udhay@123'
# server_name = 'issadsad.mydomain.in'

# import sys
# entered_args = sys.argv
# # user_name = entered_args[1]
# # password = entered_args[2]
# # server_name = entered_args[3]

# # unpacking 
# user_name, password, server_name = sys.argv[1:]

import argparse

parser = argparse.ArgumentParser(
    description="Details to login to server")
parser.add_argument('-u', '--username',
                    help='user name',
                    type=str, 
                    required=True)
parser.add_argument('-p', '--password',
                    help='password',
                    type=str, 
                    required=True)
parser.add_argument('-s', '--servername',
                    help='server name',
                    type=str, 
                    required=True)

args = parser.parse_args()


user_name = args.username
password = args.password
server_name = args.servername

print(f'''
The server login details are:
    USER NAME   : {user_name}
    PASSWORD    : {password}
    SERVER NAME : {server_name}
''')
