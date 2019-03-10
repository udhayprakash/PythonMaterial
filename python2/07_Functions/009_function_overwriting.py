#!/usr/bin/python
"""
Purpose: Function overwriting Problem


a = 10 
a = 56

"""
def myfunc(num1, num2):
    """
    Function to perform arithmetic Addition operation
    :param num1: Number
    :param num2: Number
    :return: result of addition operation
    """
    return num1 + num2



def myfunc(var1, var2, var3):
    """
    Function to perform arithmetic Multiplication operation
    :param num1: Number
    :param num2: Number
    :return: result of addition operation
    """
    return var1 + var2 + var3



print myfunc(2, 3)
print myfunc(2, 3, 5)
