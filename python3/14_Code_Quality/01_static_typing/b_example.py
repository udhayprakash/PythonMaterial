#!/usr/bin/python
"""
Purpose: Static typing with mypy

from python 3.6, mypy will come builtin. no need to import
"""


def hello(name):
    print(f'Hello {name}')


hello('Python')


# ----------------------------
def hello2(name: str) -> None:
    print(f'Hello {name}')


hello2('Python')
