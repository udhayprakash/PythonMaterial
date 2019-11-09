#!/usr/bin/python
"""
Purpose: Function overwriting Problem


a = 10
a = 56
print(a)  ? -> will be answer be 10 or 56
"""


def addition(var1, var2, var3):
    """
    This function will take three args, and return their addition
    :param var1: int
    :param var2: int
    :param var3: int
    :return: int
    """
    return var1 + var2 + var3


def addition(num1, num2):
    """
    This function will take two args, and return their addition
    :param num1: int
    :param num2: int
    :return: int
    """
    return num1 + num2


print(f'addition(10, 20)    : {addition(10, 20)}')
print(f'addition(10, 20, 30): {addition(10, 20, 30)}')
