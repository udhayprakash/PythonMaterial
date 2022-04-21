#!/usr/bin/python3
"""
Purpose: Functions Demo

    Function with default arguments

NOTE: In function definition, default args must be specified
at the end only
"""


def addition(num1, num2):
    return num1 + num2


def addition(var1, var2, var3=0):
    return var1 + var2 + var3


print(f'{addition(10, 20)     =}')
print(f'{addition(10, 20, 30) =}')

print(dir(addition))
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__',
#  '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__',
#  '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
#  '__subclasshook__']
print(f'{addition.__sizeof__() =}')
print(f'{addition.__name__     =}')
print(f'{addition.__defaults__ =}')
print()


# ======================================
# def hello():
#     print("Hello world!")
#
# # hello()
#
# def hello(name):
#     print(f"Hello {name}!")
#
# hello("Python")
# # hello()   # TypeError: hello() missing 1 required positional argument: 'name'


def hello(name='world'):
    print(f'Hello {name}!')


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
#
# SyntaxError: non-default argument follows default argument


def statement_creator(name, age=24, qualification='B.Tech'):
    """
    This is a statement creator function
    :param name: mandatory arg
    :param age:
    :param qualification:
    :return:
    """
    print(f"{name}'s age is {age}. qualification is {qualification}")


# statement_creator()
# TypeError: statement_creator() missing 1 required positional argument: 'name'
statement_creator('Udhay')
statement_creator(name='Udhay')
print()

statement_creator('Udhay', 28)
statement_creator(name='Udhay', age=28)
print()

statement_creator('Udhay', 28, 'M.Tech')
statement_creator(name='Udhay', age=28, qualification='M.Tech')

statement_creator(28)
