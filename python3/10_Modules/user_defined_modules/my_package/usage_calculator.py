#!/usr/bin/python
"""
Purpose: Importing & using python script
"""

import calculator
from calculator import division

print(dir(calculator))

# print(calculator.__builtins__)

print(f"{calculator.addition(10, 20) =}")
print()

print(f"{calculator.__doc__          =}")
print(f"{calculator.addition.__doc__ =}")
print(f"{division.__doc__            =}")


help(calculator)
print()
