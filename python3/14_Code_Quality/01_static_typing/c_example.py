#!/usr/bin/python
"""
Purpose: Static typing with mypy

from python 3.6, mypy will come builtin. no need to import
"""


# Method 1 : Traditional approach
def hello(name):
    print(f'Hello {name}')


hello('Python')

# ---------------------------------
# Method 2: Adding Typing
def hello1(name: str) -> None:
    print(f'Hello {name}')


hello1('Python')
hello1(321323)    # NO error
