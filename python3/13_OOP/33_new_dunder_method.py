#!/usr/bin/python
"""
Purpose: Importance of __new__ method
"""


# class Definition
class Person:
    def __new__(cls, *args, **kwargs):
        print("I was born")

    def __init__(self):
        print("I was named")


# Instantiation
p = Person()

# NOTE: When __new__() is defined,
# __init__() will not be called automatically

p.__init__()
