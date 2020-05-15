#!/usr/bin/python

'''
Purpose:Operator precedence
'''

# Operator precedence in python
# It follows PEMDAS rule, and left to right, and top to bottom
# P - Paranthesis
# E - Exponent
# M - Multiplication
# D - Division
# A - Addition
# S - Subtraction

# Every type of braces has importance in python
# {}  - used for dictionaries and sets
# []  - used for lists
# ()  - used of tuples; also used in arithmetic operations


result = (22 + 2 / 2 * 4 // 4 - 89) + 67 - 10e7
print
result

expression = 40 / 2
print
expression

expression = 40 / 2 / 2
print
expression

expression = 120 / 3 / 4
print
expression

expression = 120 / 4 / 3
print
expression

expression = 120 / 3 / 4 / 10
print
expression

expression = 40 / 10 // 3.0
print
expression

expression = 40 // 10 / 3.0
print
expression

expression = (40 / 10 // 3.0)  # + 23e45 - 23 + 56 * 67
print
expression
