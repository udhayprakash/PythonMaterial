#!/usr/bin/python

class Person:
    # def __new__(self):
    #     print('I am born ')

    def __init__(self):
        print('I was named')

# Instantiation
p = Person()

# NOTE: When __new__() is defined, __init__() will not be called automatically 