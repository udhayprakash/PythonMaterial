#!/usr/bin/python
"""
Purpose: Static Typing in python
    http://mypy-lang.org
python -m pip install -U mypy

python -m mypy filename.py
"""


# Using Dynamic typing 
def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


print(list(fib(10)))

# Using Static Typing
from typing import Iterator


def fib1(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


print(list(fib1(10)))


##################################

def greeting(name):
    return 'Hello ' + name


print(greeting('Python'))


def greeting1(name: str) -> str:
    return 'Hello ' + name


print(greeting1('Python'))

##########################
import typing

for ech_attr in dir(typing):
    print(ech_attr)
