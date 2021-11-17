#!/usr/bin/python3
"""
Purpose: importance and usage of argparse
"""
# # Method 1: hard- coding
# user_name = 'udhay'
# password = 'udhay@123'
# server_name = 'issadsad.mydomain.in'

# # Method 2: input() - run time
# user_name = input('Enter username:')
# password = input('Enter password:')
# server_name = input('Enter server name:')

# # # Method 3: sys.argv
# import sys
# print('sys.argv = ', sys.argv)
#
# if len(sys.argv) != 4:
#     print('Help:')
#     print(f'python {__file__} username password server_fqdn')
#     sys.exit(1)
#
# # user_name = sys.argv[1]
# # password = sys.argv[2]
# # server_name = sys.argv[3]
#
# # unpacking
# user_name, password, server_name = sys.argv[1:]


# Method 4: argparse
import argparse

parser = argparse.ArgumentParser(
    description="Details to login to server",
    epilog='-----Please follow help doc ----'
)
# description: for the text that is shown before the help text
# epilog: for the text shown after the help text


parser.add_argument('-u', '--username', help='login user name', type=str, required=True)
parser.add_argument('-p', '--password', help='login user password', type=str, required=True)
parser.add_argument('-s', '--servername', help='server name', type=str, required=False, default='www.google.com')

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
