#!/usr/bin/python
"""
Purpose: To create a class with singleton design pattern
    It means, If an instance of that class is already created,
    Instead of creating new instance, make use of already created instance
"""


class SingletonClass(object):
    __singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.__singleton:
            cls.__singleton = super().__new__(cls, *args, **kwargs)
        return cls.__singleton


class MyClass(SingletonClass):
    def __init__(self) -> None:
        # SingletonClass.__init__(self)
        super().__init__()


# Instantiation is done only once, and
# subsequent instatiations will reuse existing instance

if __name__ == "__main__":
    c1 = MyClass()
    print(f"{c1               = }")  # <__main__.MyClass object at 0x00000244B095EFE0>

    c2 = MyClass()
    print(f"{c2               = }")  # <__main__.MyClass object at 0x00000244B095EFE0>

    print(f"{id(c1) == id(c2) = }")
    assert c1 is c2
