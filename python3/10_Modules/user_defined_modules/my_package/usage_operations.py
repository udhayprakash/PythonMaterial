#!/usr/bin/python
"""
Purpose: Script for usage of operations.py
"""
import sys
import operations

sys.dont_write_bytecode = True

print(f'{operations.fibonacci(9) =}')
print(f'{operations.factorial(9) =}')
print()

# wild char import
from operations import *
print(f'{fibonacci(9) =}')
print(f'{factorial(9) =}')
