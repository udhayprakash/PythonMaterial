#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with default arguments
"""


# def addition(num1, num2):
#     return num1 + num2

def addition(var1, var2, var3=0):
    return var1 + var2 + var3

print(f'{addition(10, 20)     =}')
print(f'{addition(10, 20, 30) =}') 


# print(dir(addition))
print(f'addition.__defaults__:{addition.__defaults__}')

# -------------------------
# def hello():
#     print('Hello world!')

# hello()

# def hello(name):
#     print(f'Hello {name}')

# hello('Python')


def hello(name='world!'):
    print(f'Hello {name}')

hello()
hello('Python')



# ---------------------------------------------
# def statement_creator(age = 24, name,  qualification='B.Tech'):
#     """
#     This is a statement creator function
#     :param name: mandatory arg
#     :param age:
#     :param qualification:
#     :return:
#     """
#     print(f"{name}'s age is {age}. qualification is {qualification}")

# SyntaxError: non-default argument follows default argument
# NOTE: default args should be defined at last only

def statement_creator(name, age = 24, qualification='B.Tech'):
    """
    This is a statement creator function
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

print()
statement_creator('Udhay', 28)
statement_creator(name='Udhay', age=28)

print()
statement_creator('Udhay', 28, 'M.Tech')
statement_creator(name='Udhay', age=28, qualification='M.Tech')

