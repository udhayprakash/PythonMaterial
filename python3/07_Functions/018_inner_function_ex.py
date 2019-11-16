#!/usr/bin/python
"""
Purpose: Inner function example
Scoping - LEGB
"""

num1 = 999
mydict = {'p': 2}


# function definition
def outer():
    print('outer func -start')
    num1 = 100
    mydict = {'a': 1}

    def inner():
        print('inner func - start')
        print(f'inner, num1  ={num1}')
        print(f'inner, mydict={mydict}')

    inner()  # calling within outer() func scope


outer()
# inner() # NameError: name 'inner' is not defined
