#!/usr/bin/python
"""
Purpose: Relational Operations

 <  lesser
 >  greater
 == equal to
 <= less than or equal to
 >= greater than or equal to
 != not equal to
 <> not equal to  ( in python 2 only)
"""
us_dollar = 73
canadian_dollar = 50

print("us_dollar < canadian_dollar   ", us_dollar < canadian_dollar)
print("70 < 49      ", 70 < 49)
print("70 > 49      ", 70 > 49)

print("89 >= 49     ", 89 >= 49)
print("89 <= 49     ", 89 <= 49)

print("89 == 89     ", 89 == 89)  # don't confuse with = (assignment Operator)
# print("89 = 89", 89 = 89)   Syntax Error

print("12 != 12.0   ", 12 != 12.0)
# print("12 <> 12.1  ", 12 <> 12.1)   # SyntaxError: invalid syntax
