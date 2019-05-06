#!/usr/bin/python
"""
Purpose: Functions Demo
            - code reusability
            - To modularize the problem 
            - Better maintenance of the code 

    Functions are called as first class objects in python 

    Function with no arguments and no return value
"""
# hello()

# Function Definition
def hello():
    print("Hello world")
    #return None - default


print(hello)
print('callable(hello)', callable(hello))
fruit = 'apple'
print('callable(fruit)', callable(fruit))

# Function Call 
hello()
print(hello())
