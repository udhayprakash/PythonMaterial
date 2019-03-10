#!/usr/bin/python
'''

Purpose: Menu-Driven Bank Transactions User Interface
Usage  : python SriptName.py
'''
try:
    from colorama import Fore, Back, Style, init
except ImportError, ie:
    print ie
    print "colorama modeule is not present in this server. Installing it with pip"
    from os import system
    import sys
    if not system("pip install colorama"):
        print "Unable to install colorama on the fly"
        sys.exit(1)
    from colorama import Fore, Back, Style

__author__ = 'udhay prakash'

windowLength = 80
print Back.YELLOW
print Fore.WHITE +"_"*windowLength
print Fore.WHITE +"|"*windowLength
print Fore.WHITE +"-"*windowLength
print Back.BLUE + Style.BRIGHT +"XYZ BANK".center(windowLength)+ Back.BLACK
print Back.BLUE + Style.BRIGHT +"FINANCIAL TRANSACTION INTERFACE ".center(windowLength)
print Back.BLUE + Style.DIM + '@xyz company, interface version 0.0012'.rjust(windowLength)
print Back.WHITE
print Style.BRIGHT + Fore.BLACK+'' \
                                'FINANCIAL TRANSACTION MENU'#\
                                #+ '_'*len('FINANCIAL TRANSACTION MENU')
print Back.BLACK
print Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\n1. create an Account'\
                                '\n2. Transact from existing Account'\
                                    '\n\ta. DEPOSIT '\
                                    '\n\tb. WITHDRAW'\
                                    '\n\tc. BALANCE ENQUIRY'\
                                '\n3. Delete an existing Account '\
                                '\n4. Exit the Transaction UI'

choice = raw_input("Please Enter the interger, corresponding to your choice:")
print Back.YELLOW
print Fore.WHITE +"-"*windowLength
print Fore.WHITE +"|"*windowLength
print Fore.WHITE +"_"*windowLength
print(Style.RESET_ALL)
#print('back to normal now')


'''
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
cprint(figlet_format('XY Bank!', font='starwars'),
     'white', 'on_blue', attrs=['bold'])

'''

# while choice !=1:
