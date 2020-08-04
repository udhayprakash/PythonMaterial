#!/usr/bin/python
"""
Purpose: Exception Precedence

Python Execution flow:-
     Top to Bottom & Left to Right

"""
try:
    num1 = 10
    value = 1
    num2 = None
    expression = 11 / num1 - '0' * num2 ** value   # PEMDAS
except ZeroDivisionError as ex: 
    print(repr(ex))
except Exception as ex: 
    print(repr(ex))

# Assignment 
# Using input() and eval(), take some expression in run time and solve it 
