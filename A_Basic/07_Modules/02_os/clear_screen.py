import os
from sys import platform
def clear_screen():
    if platform in ('linux', 'linux2'): # Linux
        os.system('clear')
    else:
        os.system('cls')

clear_screen()
