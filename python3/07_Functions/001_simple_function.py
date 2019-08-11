#!/usr/bin/python
"""
Purpose: Functions Demo
            - code reusability
            - To modularize the problem 
            - Better maintenance of the code 

    Functions are called as first class objects in python 

    Function with no arguments and no return value
"""
# hello() # NameError: name 'hello' is not defined

# Function Definition
def hello():
    print("Hello world")
    #return None - default

# print(hello())

# callable()
print(f'callable(hello)   ={callable(hello)}')

language = 'python'
print(f'callable(language)={callable(language)}')
# language()  # TypeError: 'str' object is not callable

# result = hello()
# print(f'result={result}')

# First class objects 
# num1 = 123
# print(f'type(num1)       ={type(num1)}')
# print(dir(num1))
# help(num1)

print(f'hello              ={hello}')
print(f'type(hello)        ={type(hello)}')
print(f'dir(hello)         ={dir(hello)}')