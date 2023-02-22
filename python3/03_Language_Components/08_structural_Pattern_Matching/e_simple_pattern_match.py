#!/usr/bin/python3
"""
Purpose: Structural Pattern Matching
"""


def wildcardpattern(p):
    match p:
        case [_ as first, middle, _ as last]:
            print(middle)


def star_wildcard(p):
    match p:
        case [_, _, *rest]:
            print(rest)
        case {"name": _, **rest}:
            print(rest)


# >>> star_wildcard([1,2,3,4,5])
# [3, 4, 5]

# >>> star_wildcard({"name": "Cosmo", "age": 42, "last_name": "Kramer"})
# {'age': 42, 'last_name': 'Kramer'}

# wildcard with guards
match p:
    case [_, _, *rest] if sum(rest) > 10:
        print(rest)


# Value Patterns
PREFERRED_GREETING = "Hello"


def value_pattern(p):
    match p:
        case {"greeting": PREFERRED_GREETING, "name": name} as d:
            print(d)
        case _:
            print("No match!")


# >>> value_pattern({"greeting": "Salutations", "name": "Elaine"})
# {'greeting': 'Salutations', 'name': 'Elaine'}

# >>> value_pattern({"name": "Elaine"})
# No match!

import constants


def value_pattern_working(p):
    match p:
        case {"greeting": constants.PREFERRED_GREETING, "name": name} as d:
            print(d)
        case _:
            print("No match!")


# Mapping (“Dictionary”) Patterns
match {"a": 1, "b": 2}:
    case {"a": 1} as d:
        print(d)

match {"a": 1, "b": 2}:
    case {"a": 1, **rest} as d if not rest:
        print(d)

# Class Patterns
from collections import namedtuple

Customer = namedtuple("Customer", "name product")


def read_customer(p):
    match p:
        case Customer(name=name, product=product):
            print(f"{name}, you must really like {product}.")


# >>> read_customer(Customer(name="George", product="bosco"))
# George, you must really like bosco.
