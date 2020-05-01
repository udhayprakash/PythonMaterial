#!/usr/bin/python
"""
Purpose: Usage for custom module
"""

import my_module

help(my_module)

print(dir(my_module))



print(f'{my_module.__package__ =}')


my_module.newScript.firstFunction()

print(my_module.calculator.addition(89, 76))