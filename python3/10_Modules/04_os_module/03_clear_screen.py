import os
from sys import platform


def clear_screen():
    if platform == 'win32':  # windows
        output = os.system('cls')
    else:
        output = os.system('clear')
    print('output', output)


def ping_a_site(website_name):
    output = os.system(f'ping {website_name}')
    print(f'output:{output}')


if __name__ == '__main__':
    clear_screen()
    ping_a_site('google.com')

#
# # os.system('ping google.com')
# exec_result = os.system('dir')
# print(f'exec_result:{exec_result}')
