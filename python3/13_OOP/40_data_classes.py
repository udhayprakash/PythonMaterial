#!/usr/bin/python
"""
Purpose: Data classes
  Introduced in python 3.7 (with PEP 557) to reduce the boilerplate code
  For 3.6, dataclasses can be used by installing as a module
                pip install dataclasses

"""
from dataclasses import dataclass, make_dataclass
from typing import Any, List


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class Book(object):
    title: str
    author: str


# order: By default __gt__ , __ge__, __lt__, __le__ methods
# will be generated.
# If passed as False, they are omitted.

# creating a class
Position = make_dataclass("Position", ["name", "lat", "lon"])
print(type(Position))

p = Position("place", 45, 56)
print(vars(p))

##################################


@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42


m = WithoutExplicitTypes(3.14, "somethng")
print(vars(m))

#################################


@dataclass
class PlayingCard:
    rank: str
    suit: str


@dataclass
class Deck:
    cards: List[PlayingCard]


queen_of_hearts = PlayingCard("Q", "Hearts")
ace_of_spades = PlayingCard("A", "Spades")

two_cards = Deck([queen_of_hearts, ace_of_spades])
print(two_cards)
print(vars(two_cards))

########################################
# INHERITANCE


@dataclass
class Position:
    name: str
    lon: float
    lat: float


@dataclass
class Capital(Position):
    country: str


c = Capital("Oslo", 10.8, 59.9, "Norway")
print(c)
print(vars(c))
