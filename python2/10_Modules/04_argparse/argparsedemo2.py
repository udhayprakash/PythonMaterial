from __future__ import print_function
import argparse

def login(user_name, password, email_address):
    """
    print the login details
    :param user_name:
    :param password:
    :param email_address:
    :return:
    """
    print("USERNAME:", user_name)
    print("PASSWORD:", password)
    print("EMAIL ID:", email_address)


# print '__name__', __name__

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Script to get the user credetials and display them")
    parser.add_argument('-user',
                        help='Username')
    parser.add_argument('-passwrd',
                        help='Password')
    parser.add_argument('-email',
                        help='Email address')
    args = parser.parse_args()

    login(args.user, args.passwrd, args.email)
