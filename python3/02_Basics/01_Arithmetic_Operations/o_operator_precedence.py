#!/usr/bin/python
"""
Purpose: Operator precedence in python

    Python Execution Flow:
        left to right, and top to bottom

    It follows PEMDAS rule, and execution flow
        P - Paranthesis
        E - Exponent
        M - Multiplication
        D - Division
        A - Addition
        S - Subtraction

    Every type of braces has importance in python
    {}  - used for dictionaries and sets
    []  - used for lists
    ()  - used of tuples; also used in arithmetic operations
"""

result = (22 + 2 / 2 * 4 // 4 - 89) + 67 - 10e7
# result = (22 + 2 / 8 // 4 - 89) + 67 - 10e7
print(result)

expression = 40 / 2
print(result)

expression = 40 / 2 / 2
print(result)

expression = 120 / 3 / 4
print(result)

expression = 120 / 4 / 3
print(result)

expression = 120 / 3 / 4 / 10
print(result)

expression = 40 / 10 // 3.0
print(result)

expression = 40 // 10 / 3.0
print(result)

expression = 40 / 10 // 3.0  # + 23e45 - 23 + 56 * 67
print(result)

result = (True == False) in (False,) == False
print(result)
