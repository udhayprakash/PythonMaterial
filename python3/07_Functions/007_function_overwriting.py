#!/usr/bin/python
"""
Purpose: Function overwriting Problem


a = 10 
a = 56
print(a)
"""
   
def myfunc(var1, var2, var3):
    """
    Function to perform arithmetic Multiplication operation
    :param num1: Number
    :param num2: Number
    :return: result of addition operation
    """
    return var1 + var2 + var3

def myfunc(num1, num2):
    """
    Function to perform arithmetic Addition operation
    :param num1: Number
    :param num2: Number
    :return: result of addition operation
    """
    return num1 + num2
 

print('myfunc(2, 3)   =', myfunc(2, 3))
print('myfunc(2, 3, 5)=', myfunc(2, 3, 5))
