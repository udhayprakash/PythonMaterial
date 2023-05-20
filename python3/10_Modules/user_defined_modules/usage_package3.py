#!/usr/bin/python
"""
Purpose: Importing & using python script
"""
import package3

print(dir(package3))

print(package3.__doc__)
print(package3.calculator.__doc__)
print(package3.operations.__doc__)
print()

print(package3.calculator.addition.__doc__)
print()

from package3 import calculator
from package3.calculator import division

print(dir(calculator))

# print(calculator.__builtins__)

print(f"{calculator.addition(10, 20) =}")
print()

print(f"{calculator.__doc__          =}")
print(f"{calculator.addition.__doc__ =}")
print(f"{division.__doc__            =}")


help(calculator)
