#!/usr/bin/python3
"""
Purpose: Inner function example
    Scoping - LEGB
"""
from math import pi   # Builtin 
pi = 300              # Global
mydict = {'lang': 'python'}

def outer(given):
    print('outer function - start ')
    pi = 200            # Local for outer()
    mydict = {'lang': 'ruby'}
    # inner() # UnboundLocalError: local variable 'inner' referenced before assignment
    
    def inner():
        print('inner function - start')
        pi = 100        # Local for inner()
        mydict = {'lang': 'golang'}
        print(f'{pi             = }')
        print(f'{mydict["lang"] =}')
    
    if given % 2 == 0:
        inner()

print(f'{globals().keys() =}')
outer(124)
# inner() # NameError: name 'inner' is not defined
