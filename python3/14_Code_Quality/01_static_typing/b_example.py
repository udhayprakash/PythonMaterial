#!/usr/bin/python
"""
Purpose: Static typing with mypy

from python 3.6, mypy will come builtin. no need to import
"""


# Method 1 : Traditional approach
def hello():
    print("Hello world")


hello()

# -------------------------------------
# Method 2: Adding typing
def hello() -> None:
    print("Hello world")


hello()
