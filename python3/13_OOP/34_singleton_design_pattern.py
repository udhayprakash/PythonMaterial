#!/usr/bin/python
"""
Purpose: To create a class with singleton design pattern
    It means, If an instance of that class is already created,
    Instead of creating new instance, make use of already created instance
"""


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
