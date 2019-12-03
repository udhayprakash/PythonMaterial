#!/usr/bin/python
"""
Purpose: decorator example
"""


def decortor_func1(func):
    def wrapper(*args, **kwargs):
        print(' I am  in decorator 1')
        func(*args, **kwargs)

    return wrapper


def decortor_func2(func):
    def wrapper(*args, **kwargs):
        print(' I am  in decorator 2')
        func(*args, **kwargs)

    return wrapper

# NOTE: decorator will be executed top to bottom order


@decortor_func1
@decortor_func2
def actual_function():
    print('I am actual function')


actual_function()
