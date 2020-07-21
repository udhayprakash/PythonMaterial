#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with two arguments and no return value
"""

# Function Definition
def hello(name, age):
    print(f"{name}'s age is {age}")

# Function call
# hello()
# TypeError: hello() missing 2 required positional arguments: 'name' and 'age'

# hello('SUresh')
# TypeError: hello() missing 1 required positional argument: 'age'

print('\ncall By position')
hello('SUresh', 34)  
hello(34, 'SUresh')

print('\ncall By keyword args')
hello(name='Suresh', age=34)
hello(age=34, name='Suresh')