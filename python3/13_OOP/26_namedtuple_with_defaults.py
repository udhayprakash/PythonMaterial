#!/usr/bin/python
"""
Purpose: Named tuple with default values

"""
from typing import NamedTuple

class Person(NamedTuple):
    name: str 
    age : int 
    DOB:  str 
    phone_required: bool = False 

p1 = Person('Gudo Vann RUssum', 72, '1/1/1900', phone_required=True)
print(p1)
print(type(p1))
print(dir(p1))