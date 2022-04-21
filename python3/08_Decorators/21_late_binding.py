#!/usr/bin/python3
"""
Purpose: Late Binding

"""


from operator import mul
from functools import partial


def problem():
    """Late binding - all functions will get last value .
    Because values of variables used in closures are looked up at the time of
    calling the inner function."""
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in problem()])  # [6, 6, 6, 6]


def solution():
    """Solution - Local variable is created"""
    return [lambda x, i=i: i * x for i in range(4)]


print([m(2) for m in solution()])  # [0, 2, 4, 6]


# ---------------------
def create_multipliers():
    multipliers = []

    for i in range(5):

        def multiplier(x):
            return i * x

        multipliers.append(multiplier)

    return multipliers


print([m(2) for m in create_multipliers()])  # [8, 8, 8, 8, 8]


def create_multipliers():
    return [partial(mul, i) for i in range(5)]


print([m(2) for m in create_multipliers()])  # [0, 2, 4, 6, 8]


# PS: In some cases, this late binding is advantageous
