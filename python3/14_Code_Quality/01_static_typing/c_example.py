#!/usr/bin/python
"""
Purpose: Static typing with mypy

from python 3.6, mypy will come builtin. no need to import
"""


def hello(name):
    return f'Hello {name}'


result = hello('Python')
print(result)


# ----------------------------
def hello3(name: str) -> str:
    return f'Hello {name}'


result = hello3('Python')
print(result)

# ----------------------------
from typing import Any


def hello4(name: Any) -> str:
    return f'Hello {name}'


result = hello4('Python')
print(result)
result = hello4(32123213)
print(result)
