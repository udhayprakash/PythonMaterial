#!/usr/bin/python
"""
Purpose: Static typing with mypy

from python 3.6, mypy will come builtin. no need to import
"""


# Method 1 : Traditional approach
def hello(name):
    return f'Hello {name}'


result = hello('Python')
print(result)


# -------------------------------
# Method 2 : Adding Typing
def hello(name: str) -> str:
    return f'Hello {name}'


result = hello('Python')
print(result)
