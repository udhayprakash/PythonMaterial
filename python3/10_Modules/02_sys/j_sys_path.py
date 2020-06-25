#!/usr/bin/python
"""
Purpose: sys.path 
    - Gives the paths to refer
    Scope Resolution - LEGB 
        - Buitin 

"""
from fibonacci_series import fib
from calculator import add
import sys
# print(sys.path) # gives a list of paths

sys.path.insert(0,
                r'D:\MEGAsync\Python-related\training\python_related\python_batch154\07_Functions')

for each_path in sys.path:
    print(each_path)

# NOTE: Installed modules are stored in "site-packages"

sys.dont_write_bytecode = True
# pycache files are not created when it is True

print(f'{add(12, 10) =}')

print(f'{fib(5) =}')


# Assignments 
# Try to add and use with relative path 
# sys.path.insert(0, r'..\..\07_Functions')
