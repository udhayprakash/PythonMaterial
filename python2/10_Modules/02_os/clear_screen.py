import os
from sys import platform

def clear_screen():
    if platform in ('linux', 'linux2', 'darwin'): # Linux
        output = os.system('clear')
    else:
        output = os.system('cls')
    print 'output', output
    
clear_screen()
