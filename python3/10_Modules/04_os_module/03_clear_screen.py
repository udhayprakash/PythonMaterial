import os
from sys import platform


def clear_screen():
    if platform == 'win32':  # windows
        output = os.system('cls')
    else:
        output = os.system('clear')
    print('output', output)


clear_screen()

# os.system('ping google.com')
exec_result = os.system('dir')
print(f'exec_result:{exec_result}')
