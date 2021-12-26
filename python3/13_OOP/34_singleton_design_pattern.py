#!/usr/bin/python
"""
Purpose: To create a class with singleton design pattern
    It means, If an instance of that class is already created,
    Instead of creating new instance, make use of already created instance
"""
from pprint import pprint

# Question: __new__ vs __init__
# baby born   => __new__
# baby named  => __init__


class Logger(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._logger


l1 = Logger()
pprint(vars(Logger))

print(f'l1:{l1}')
print(vars(l1))

l2 = Logger()
print(id(l1), id(l2))

assert l1 is l2

# ------------------------------------


class Base(object):
    __singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.__singleton:
            cls.__singleton = super(Base, cls).__new__(cls, *args, **kwargs)
        return cls.__singleton


class MyClass(Base):
    def __init__(self) -> None:
        Base.__init__(self)


c1 = MyClass()
print(c1)  # <__main__.MyClass object at 0x00000244B095EFE0>

c2 = MyClass()
print(c2)  # <__main__.MyClass object at 0x00000244B095EFE0>
