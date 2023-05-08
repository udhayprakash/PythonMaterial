#!/usr/bin/python3
"""
Purpose: Currying Functions

    - Inner functions are functions defined inside another function that can be used for various purposes, while
      currying is a technique that transforms a function that takes multiple arguments into a sequence of functions that each take a single argument.
    - Inner functions can be used to create closures, encapsulate helper functions, or implement decorators, while
      currying is useful for creating more flexible and composable functions in functional programming.
    - While inner functions can be used to implement currying, they are not the same thing, and
      currying can also be implemented using other techniques such as lambda functions or partial function application.
"""


# Example of inner functions
def outer(x):
    def inner(y):
        return x + y

    return inner


add5 = outer(5)
print(add5(3))  # Output: 8


# Example of currying using lambda functions
def add(x):
    return lambda y: x + y


add5 = add(5)
print(add5(3))  # Output: 8


# ------------------------------------------------------------


# Example of inner functions
def multiply_by(x):
    def inner(y):
        return x * y

    return inner


double = multiply_by(2)
print(double(5))  # Output: 10


# Example of currying using lambda functions
def multiply(x):
    return lambda y: x * y


triple = multiply(3)
print(triple(5))  # Output: 15


# --------------------------------------------------------------
# Example of inner functions
def compose(f, g):
    def inner(x):
        return f(g(x))

    return inner


def square(x):
    return x * x


def add(x):
    return x + 1


square_and_add = compose(add, square)
print(square_and_add(3))  # Output: 10

# Example of currying using partial function application
from functools import partial


def compose(f, g, x):
    return f(g(x))


square_and_add = partial(compose, add, square)
print(square_and_add(3))  # Output: 10
