#!/usr/bin/python
"""
Purpose: Static typing with mypy

from python 3.6, mypy will come builtin. no need to import
"""


# ----------------------------
def hello():
    print('Hello world')


hello()


# ----------------------------
def hello1() -> None:
    print('Hello world')


hello1()


