#!/usr/bin/python
"""
Purpose: functools.total_ordering
    - provide a way to provide automatic comparison functions.
    - conditions
        1. Definition of at least one comparison function is
           a must like le, lt, gt or ge.
        2. Definition of eq function is mandatory.
"""
import random
from functools import total_ordering


@total_ordering
class Number:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self) -> str:
        return f"{self.value}"


print(f"{Number(1) < Number(2)   =}")
print(f"{Number(10) > Number(21) =}")
print(f"{Number(10) <= Number(2) =}")  # less than or equal
print(f"{Number(10) >= Number(20)=}")  # greater than
print(f"{Number(2) <= Number(2)  =}")
print(f"{Number(2) >= Number(2)  =}")
print(f"{Number(2) == Number(2)  =}")
print(f"{Number(2) == Number(3)  =}")

values = []
for i in range(10, 20):
    values.append(Number(i))

print(values)
print(sorted(values))
