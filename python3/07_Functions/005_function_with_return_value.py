#!/usr/bin/python3
"""
Purpose: Functions Demo

    Function with two arguments and default return value
NOTE: return is the last statement in function execution

"""
# Function Definition


def addition(n1, n2):
    result = n1 + n2
    # return
    # return 'None'
    # return 'Hello world'
    # print('12312123')
    # return result
    # return 123
    # return 123.
    # return 123.23
    # return 123.23,
    # return 123.23,, # SyntaxError: invalid syntax
    # return (123.23,),
    # return n1 + n2
    return 12 - 123 * 23 / 3 // 23


# NOTE:
# 1. By default, function return is None
# Function call
addition(12, 13)

answer = addition(12, 13)
print(type(answer), answer)
