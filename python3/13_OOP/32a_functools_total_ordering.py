#!/usr/bin/python
"""
Purpose: functools.total_ordering
    - provide a way to provide automatic comparison functions.
    - conditions
        1. Definition of at least one comparison function is
           a must like le, lt, gt or ge.
        2. Definition of eq function is mandatory.
"""

from functools import total_ordering


@total_ordering
class Number:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


print(f'{Number(1) < Number(2)   =}')
print(f'{Number(10) > Number(21) =}')
print(f'{Number(10) <= Number(2) =}')
print(f'{Number(10) >= Number(20)=}')
print(f'{Number(2) <= Number(2)  =}')
print(f'{Number(2) >= Number(2)  =}')
print(f'{Number(2) == Number(2)  =}')
print(f'{Number(2) == Number(3)  =}')
