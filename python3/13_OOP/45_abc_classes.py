#!/usr/bin/python
"""
Purpose: Abstract Classes
    - classes that contain one or more abstract methods.
    - abstract method
        - method that is declared, but contains no implementation.
    - Abstract classes cannot be instantiated, and require subclasses
      to provide implementations for the abstract methods.
"""


# Ordinary classes
class AbstractClass:
    def do_something(self):
        pass


class B(AbstractClass):
    pass


a = AbstractClass()
b = B()
# do_something() method will be inherited in b,
# and no need to define it
b.do_something()
# ---------------------------------------------------

from abc import ABC, abstractmethod


class AbstractClassExample(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass


class DoAdd42(AbstractClassExample):
    pass


# x = DoAdd42(4)
# TypeError: Can't instantiate abstract class DoAdd42 with abstract methods do_something

# -----------------------------------------------------
class DoAdd42(AbstractClassExample):
    def do_something(self):
        return self.value + 42


class DoMul42(AbstractClassExample):
    def do_something(self):
        return self.value * 42


x = DoAdd42(10)
y = DoMul42(10)

print(x.do_something())
print(y.do_something())
