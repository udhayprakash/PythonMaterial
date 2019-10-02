#!/usr/bin/python
"""
Purpose: Data classes 
  Introduced in python 3.7 (with PEP 557) to reduce the boilerplate code 
  For 3.6, dataclasses can be used by installing as a module 
                pip install dataclasses

"""
from dataclasses import dataclass


@dataclass()
class Foo(object):
    x: int


f = Foo(12)
print(f.x)
f.x = 1
f.y = 12

# print(hash(f)) # TypeError: unhashable type: 'Foo'

print('With FROZEN =============')


@dataclass(frozen=True)
class Foo(object):
    x: int


f = Foo(12)
print(f.x)
# f.x = 1
print(hash(f))

# NOTE: Namedtuples are also dataclasses, 
# but immutable by default
