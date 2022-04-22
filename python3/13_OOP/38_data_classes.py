#!/usr/bin/python
"""
Purpose: Data classes
  Introduced in python 3.7 (with PEP 557) to reduce the boilerplate code
  For 3.6, dataclasses can be used by installing as a module
                pip install dataclasses

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
