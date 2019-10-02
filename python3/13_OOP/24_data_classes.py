#!/usr/bin/python
"""
Purpose: Data classes 
  Introduced in python 3.7 (with PEP 557) to reduce the boilerplate code 
  For 3.6, dataclasses can be used by installing as a module 
                pip install dataclasses

"""
import random
from dataclasses import dataclass, field


def random_price():
    return random.randint(20, 100)


@dataclass
class Book(object):
    title: str
    author: str
    price: float = field(default_factory=random_price)


b = Book('Python programmig', 'David Beazley')
print(vars(b))

# Note that you cannot both set default_factory 
# and a default value; the whole point is that 
# default_factory lets you run a function and, 
# thus, provides the value dynamically, when the new instance is created.
