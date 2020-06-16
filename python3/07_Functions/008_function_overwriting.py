#!/usr/bin/python
"""
Purpose: Function overwriting Problem
    Python doesnt support function overloading

a = 10
a = 56
print(a)  ? -> will be answer be 10 or 56
"""

# Case 1
def addition(var1, var2, var3):
    return var1 + var2 + var3


def addition(num1, num2):
    return num1 + num2

print(f'{addition(10, 20)     =}')
# print(f'{addition(10, 20, 30) =}')  
# TypeError: addition() takes 2 positional arguments but 3 were given

print()
# Case 2
def addition(num1, num2):
    return num1 + num2

def addition(var1, var2, var3):
    return var1 + var2 + var3

print(f'{addition(10, 20, 30) =}')  
# print(f'{addition(10, 20)     =}')
# TypeError: addition() missing 1 required positional argument: 'var3'