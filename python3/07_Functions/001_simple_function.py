#!/usr/bin/python
"""
Purpose: Functions Demo
            - code reusability
            - To modularize the problem 
            - Better maintenance of the code 

    Functions are called as first class objects in python 

    Function with no arguments and no return value
"""

# hello()  # NameError: name 'hello' is not defined


# Function definition
def hello():
    print('hello function is called')


# NOTE: default function return is None


# Function call
print(hello())

# callability of an object - callable()
print(f'callable(hello)  :{callable(hello)}')
print(f'callable(hello()):{callable(hello())}')

word = 'python'  # string
print(f'callable(word)   :{callable(word)}')


# Functions are treated as first class objects
num1 = 12.32
print(num1, id(num1))
print(f'type(num1)      : type(num1)')
print(dir(num1))  #  attributes for float

print(hello,  id(hello))
print(f'type(hello)      : type(hello)')
print(dir(hello)) # attributes for function
