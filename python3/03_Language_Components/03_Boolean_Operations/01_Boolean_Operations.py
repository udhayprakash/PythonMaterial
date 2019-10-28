#!/usr/bin/python
"""
Purpose: Boolean Operations

    True, False
"""

choice = True
print('choice = ', choice, type(choice))

choice = False
print('choice = ', choice, type(choice))


true = 'Udhay Prakash'  # NOT RECOMMENDED to use 'true' for variable name

choice = true
print('choice = ', choice, type(choice))

# Object 
#  - address location where it is stored - id()
#  - type(s)
#  - value(s)

print("id(True)     = ", id(True))
print("id(true)     = ", id(true))

print("type(True)   =", type(True))
print("type(true)   =", type(true))

print("True         = ", True)
print("True * 30    = ", True * 30)  # True has a value of one

print("False        = ", False)
print("False * 30   = ", False * 30)  # False has a value of zero
