#!/usr/bin/python
"""
Purpose: getpass
    - Mainly to get the sentivite information
        in concealed way
"""
import getpass

# print(dir(getpass))

print(f"{getpass.getuser() =}")

user_name = input("Enter user name:")
# pass_word = input('Enter password :')
pass_word = getpass.getpass("Enter password :")

print(
    f"""
    Entered Details
        {user_name =}
        {pass_word =}
"""
)
