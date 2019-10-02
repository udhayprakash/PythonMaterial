#!/usr/bin/python
"""
Purpose: Data classes 
  Introduced in python 3.7 (with PEP 557) to reduce the boilerplate code 
  For 3.6, dataclasses can be used by installing as a module 
                pip install dataclasses

"""


class UsingRegularClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.name!r}, suit={self.age!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.name, self.age) == (other.name, other.age)


a = UsingRegularClass('Udhay', 30)
print(a)
# print(a.__repr__())
# print(dir(a))

print('-' * 80)

from dataclasses import dataclass


@dataclass
class UsingDataClass:
    name: str
    age: str


b = UsingDataClass('Udhay', 30)
print(b)
# print(dir(b))

print(a == b)


##################################
@dataclass
class ArithmeticOperations:
    num1: int
    num2: int

    def addition(self):
        return self.num1 + self.num2


a = ArithmeticOperations(123, 345)
# print(dir(a))
print(f'a.addition():{a.addition()}')


##################################
@dataclass
class ArithmeticOperations:

    def addition(self, num1, num2):
        return num1 + num2


a = ArithmeticOperations()
print(f'a.addition(123, 345):{a.addition(123, 345)}')
