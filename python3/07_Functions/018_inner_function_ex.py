#!/usr/bin/python
"""
Purpose: Inner function example
Scoping - LEGB
"""
from math import pi

pi = 300
mydict = {'lang': 'python'}


# function definition
def outer(given):
    print('outer function - start ')
    pi = 200
    mydict = {'lang': 'ruby'}

    def inner():
        pi = 100
        mydict = {'lang': 'golang'}
        print('inner function - start')
        print(f'pi              :{pi}')
        print(f'mydict["lang"]  :{mydict["lang"]}')

    if given % 2 == 0:  # even:
        inner()


# function call
if __name__ == '__main__':
    outer(123)
