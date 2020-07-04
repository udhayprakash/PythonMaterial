#!/usr/bin/python
"""
Purpose: Named tuple with default values

"""
# from dataclasses import dataclass
from typing import NamedTuple

# @dataclass
class Person(NamedTuple):
    name: str
    age: int
    DOB: str
    phone_required: bool = False


p1 = Person('Gudo Vann Russum', 72, '1/1/1900', phone_required=True)
print(p1)
print(type(p1))
# print(dir(p1))

print(f'{p1._fields   =}')
print(f'{p1._asdict() =}')
