#!/usr/bin/python
"""
Purpose: Encapsulation in OOP
    Name Mangling
        _var     protected variable
        __var    private variable
        __var__  built-in variable
"""
from pprint import pprint


class Car:
    a = 'public class variable'
    _a = 'protected class variable'
    __a = 'private class variable'

    def __init__(self):
        self.b = 'Public Instance variable'
        self._b = 'Protected Instance Variable'
        self.__b = 'Private Instance Variable'

    def instance_method(self):
        print('Public Instance method')

    def _instance_method(self):
        print('Protected Instance method')

    def __instance_method(self):
        print('Private Instance method')

    def new_method(self):
        """
        Within the class definition, private variables/methods
        can be accessed directly, withput name mangling
        :return:
        """
        print(f'self.__b                : {self.__b}')
        print(f'self.__instance_method(): {self.__instance_method()}')
        print(f'Car.__a                 : {Car.__a}')


c = Car()
pprint(vars(Car))
print('Car.a      ', Car.a)  # accessing pubic variable
print('Car._a     ', Car._a)  # accessing protected variable

# print('Car.__a', Car.__a) # accessing private variable
print('Car._Car__a', Car._Car__a)  # accessing private variable

print()

pprint(vars(c))

print()
print(f'c.b         :{c.b}')
print(f'c._b        :{c._b}')
print(f'c._Car__b   :{c._Car__b}')
print()

c.instance_method()  # public
c._instance_method()  # protected
c._Car__instance_method()  # Private

print()
c.new_method()