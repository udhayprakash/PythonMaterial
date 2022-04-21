#!/usr/bin/python3
"""
Purpose: sys.path
    - Gives the paths to refer
    Scope Resolution - LEGB
        - Builtin

"""
import sys

# print(sys.path) # gives a list of paths

for each_path in sys.path:
    print(each_path)

# NOTE: Installed modules are stored in "site-packages"

# Case 1
from j_calculator import add

print(f'{add(10, 20) = }')

# Case 2
from myfolder import myops

print(f'{myops.factorial(10) =}')

# Case 3
from myfolder.myops import factorial

print(f'{factorial(10) =}')

# import c_coroutines
# ModuleNotFoundError: No module named 'c_coroutines'
sys.path.append(
    r'D:\MEGAsync\Python-related\training\python_related\python_UK_Sept_2021\09_Iterators_Generators_Coroutines\04_Couroutines')

print(f'{sys.path[-1] =}')

sys.dont_write_bytecode = True
# pycache files are not created when it is True

import c_coroutines as cc

print(dir(cc))

print(f'{cc.__cached__      = }')
print(f'{cc.__doc__         = }')
print(f'{cc.__file__        = }')
print(f'{cc.__loader__      = }')
print(f'{cc.__name__        = }')
print(f'{cc.__package__     = }')
print(f'{cc.__spec__        = }')
print(f'{cc.my_coroutine    = }')

# Assignments
# Try to add and use with relative path
# sys.path.insert(0, r'..\09_Iterators_Generators_Coroutines')
