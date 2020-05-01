#!/usr/bin/python
"""
Purpose: importing python script and using as a module
"""
# import os 
# print(os.getcwd())
# print(os.listdir())

# import calculator
import calculator as cal

print(dir(cal))

# ['__builtins__', '__cached__', '__doc__', '__file__', 
# '__loader__', '__name__', '__package__', '__spec__', 
# 'addition', 'division', 'multipliation', 'subtraction']


print(f'{cal.__file__ =}')
print(f'{cal.__name__ =}')
print()

print(f'{cal.__doc__ =}')
print(f'{cal.addition.__doc__ =}')
print()

print(f'{cal.addition(99, 1)      =}')
print(f'{cal.subtraction(99, 1)   =}')
print(f'{cal.multipliation(99, 1) =}')
print(f'{cal.division(99, 1)      =}')
