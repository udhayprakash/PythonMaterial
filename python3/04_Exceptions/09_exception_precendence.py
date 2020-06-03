#!/usr/bin/python
"""
Purpose: Exception Precedence

Python Execution flow:-
     Top to Bottom & Left to Right

"""
try:
    expression = 11 / 0 - '0' * None ** value   # PEMDAS
except ZeroDivisionError as ex: 
    print(repr(ex))
except Exception as ex: 
    print(repr(ex))

# Assignment 
# Using input() and eval(), take some expression in run time and solve it 
