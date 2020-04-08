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


# =========================
# Method 1 : Traditional Approach
def mirror(name):
    return str(name)


print(mirror(100))
print(mirror(123.453))
print(mirror(True))
print(mirror(None))

# ----------------------------
# Method 2: Adding typing
from typing import Any


def mirror(name: Any) -> str:
    return str(name)


print(mirror(100))
print(mirror(123.453))
print(mirror(True))
print(mirror(None))
