#!/usr/bin/python
"""
Purpose: To create a class with singleton design pattern
    It means, If an instance of that class is already created,
    Instead of creating new instance, make use of already created instance
    Or not allowing new instance creation
"""
from pprint import pprint


class Singleton(Exception):
    __single = None

    def __init__(self):
        if Singleton.__single:
            raise Singleton.__single
        Singleton.__single = self


s = Singleton()
pprint(vars(Singleton))
print()

# Doesnt allow to create second instance
d = Singleton()

# ----


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
