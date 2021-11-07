#!/usr/bin/python3
"""
Purpose: Decorator Hierarchy
"""


def decorator_func1(func):
    def wrapper(*args, **kwargs):
        print("I am in decorator 1")
        func(*args, **kwargs)

    return wrapper


def decorator_func2(func):
    def wrapper(*args, **kwargs):
        print("I am in decorator 2")
        func(*args, **kwargs)

    return wrapper


def decorator_func3(func):
    def wrapper(*args, **kwargs):
        print("I am in decorator 3")
        func(*args, **kwargs)

    return wrapper


# --------------------------
@decorator_func3
@decorator_func2
@decorator_func1
def actual_function():
    print('I am actual function')


actual_function()

# NOTE: decorator will be executed top to bottom order
