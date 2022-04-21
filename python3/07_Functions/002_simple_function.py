#!/usr/bin/python3
"""
Purpose: Defining functions

NOTE: default function return is None
"""


# Type 1: Function with no arguments and no return value

# Function Definition
def hello():
    print('hello function is called')


# Function call
hello()
print(hello())  # default function return is None

# callability of an object - callable()
print(f'callable(hello)  :{callable(hello)}')

print(f'callable(hello()):{callable(hello())}')
print(f'callable(None)   :{callable(None)}')

word = 'python'  # string
print(f'callable(word)   :{callable(word)}')
# word()  # TypeError: 'str' object is not callable

print()
# Functions are treated as "first class objects"
num1 = 122.13
print(f'''
        {num1       =}
        {type(num1) =}
        {id(num1)   =}
        {dir(num1)  =}

''')

print(f'''
        {hello       =}
        {type(hello) =}
        {id(hello)   =}
        {dir(hello)  =}
''')
