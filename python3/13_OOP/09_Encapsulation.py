#!/usr/bin/env python
"""
Purpose: Encapsulation
            Name mangling
"""
from pprint import pprint


class Car:
    a = 'public class variable'
    _a = 'protected class variable'
    __a = 'private class variable'

    def __init__(self):
        self.b = 'Public Instance Variable'
        self._b = 'Protected Instance Variable'
        self.__b = 'Private Instance Variable'

    def instance_method(self):
        print('Public Instance method')

    def _instance_method(self):
        print('Protected Instance method')

    def __instance_method(self):
        print('Private Instance method')

    def new_method(self):
        print(f'self.__b                : {self.__b}')
        print(f'self.__instance_method(): {self.__instance_method()}')
        print(f'Car.__a                 : {Car.__a}')


c = Car()
pprint(vars(Car))

print('Car.a ', Car.a)  # accessing pubic variable
print('Car._a', Car._a)  # accessing protected variable

# print('Car.__a', Car.__a) # accessing private variable
print('Car._Car__a', Car._Car__a)  # accessing private variable

print()
pprint(vars(c))

print(f'c.b         :{c.b}')
print(f'c._b        :{c._b}')
print(f'c._Car__b   :{c._Car__b}')

print()
c.instance_method()  # public
c._instance_method() # protected
c._Car__instance_method() # Private

print()
c.new_method()
