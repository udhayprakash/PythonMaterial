#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with default arguments
"""


# def addition(num1, num2):
#     """
#     This function will take two args, and return their addition
#     :param num1: int
#     :param num2: int
#     :return: int
#     """
#     return num1 + num2

def addition(var1, var2, var3=0):
    """
    This function will take two/three args, and return their addition
    :param var1: int
    :param var2: int
    :param var3: int - optional
    :return: int
    """
    return var1 + var2 + var3


print(f'addition(10, 20)    : {addition(10, 20)}')
print(f'addition(10, 20, 30): {addition(10, 20, 30)}')

print(dir(addition))
print(f'addition.__defaults__:{addition.__defaults__}')


# ---------------------------------
# def hello():
#     print('Hello world!')
#
#
# hello()
#
#
# def hello(name):
#     print(f'Hello {name}!')
#
#
# hello('python')

def hello(name='world'):
    print(f'Hello {name}!')


hello()  # Hello world!
hello('python')  # Hello python!


# ---------------------------------------------
# NOTE: default args should be defined at last only
def statement_creator(name, age=25, qualification='B.Tech'):
    """

    :param name: mandatory arg
    :param age:
    :param qualification:
    :return:
    """
    print(f"{name}'s age is {age}. qualification is {qualification}")


print(f'statement_creator.__defaults__  :{statement_creator.__defaults__}')
print(f'statement_creator.__kwdefaults__:{statement_creator.__kwdefaults__}')

# statement_creator() # TypeError: statement_creator() missing 1 required positional argument: 'name'
statement_creator('Udhay')
statement_creator(name='Udhay')
statement_creator(name='Udhay', age=28)
