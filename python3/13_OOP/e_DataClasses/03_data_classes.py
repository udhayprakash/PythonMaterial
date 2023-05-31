#!/usr/bin/python
"""
Purpose: Data classes
"""
from dataclasses import asdict, astuple, dataclass


@dataclass
class Book(object):
    title: str
    author: str
    price: float = 20  # default value


b = Book("Python", "Mark Lutz")
print(f"{vars(b)   =}")
print(f"{asdict(b) =}")

print(f"{astuple(b)=}")
