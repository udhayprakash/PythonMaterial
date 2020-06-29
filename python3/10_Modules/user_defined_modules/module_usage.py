#!/usr/bin/python
"""
Purpose: usage for user-defined package 
"""
import my_package

print(f'{my_package.__name__    =}')
print(f'{my_package.__doc__     =}')
# print(f'{my_package.__file__    =}')
# print(f'{my_package.__path__    =}')
print(f'{my_package.__package__ =}')
print()
print(dir(my_package))

print(f'{my_package.calculator.DOZEN            =}')
print(f'{my_package.calculator.addition(10, 20) =}')

print(f'{my_package.operations.factorial(8)     =}')