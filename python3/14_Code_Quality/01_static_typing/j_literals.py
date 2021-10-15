#!/usr/bin/python3
"""
Purpose: Literal 
    - to restrict to a specific values ONLY
    - introduced in python 3.8
"""
from dataclasses import dataclass
from typing import Literal


@dataclass
class Person:
    name: str
    Age: int
    married: bool


print(f'{Person("Ram", 0, True)    =}')
print(f'{Person("shyam", 5, False) =}')


@dataclass
class Person2:
    name: Literal["Ram", "Robert"]
    Age: Literal[0, 1, 2]
    married: bool


print(f'{Person2("Ram", 0, True)  =}')
print(f'{Person2("Ram", 5, False) =}')
print(f'{Person2("shyam", 2, False) =}')

# python -m mypy j_literals.py
