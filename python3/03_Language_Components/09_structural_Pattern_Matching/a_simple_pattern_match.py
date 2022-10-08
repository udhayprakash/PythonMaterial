#!/usr/bin/python3
"""
Purpose: Structural Pattern Matching
    - new in python 3.10
    - Syntax:
        match <expression>:
            case <pattern 1> [<if guard>]:
                <handle pattern 1>
            case <pattern n> [<if guard>]:
                <handle pattern n>
"""
from enum import Enum


def literal_pattern(p):
    match p:
        case 1:
            print("You said the number 1")
        case 42:
            print("You said the number 42")
        case "Hello":
            print("You said Hello")
        case True:
            print("You said True")
        case 3.14:
            print("You said Pi")
        case _:
            print("You said something else")


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


print(f"{http_error(400) =}")
print(f"{http_error(404) =}")
print(f"{http_error(300) =}")
print()


def http_error(status):
    match status:
        case 401 | 403:
            return "Not allowed"
        case 404 | 405:
            return "Should not Allow"
        case _:
            return "Something's wrong with the internet"


print(f"{http_error(400) =}")
print(f"{http_error(404) =}")
print(f"{http_error(300) =}")

# -----------
def as_pattern(p):
    match p:
        case int() as number:
            print(f"You said a {number=}")
        case str() as string:
            print(f"Here is your {string=}")


# >>> as_pattern("Inspired Python")
# Here is your string='Inspired Python'
# >>> as_pattern(42)
# You said a number=42


# Patterns with a literal and variable
point = (1, 0)
point = (1, 2)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")


# Patterns and classes¶
class Point:
    x: int
    y: int


def location(point):
    match point:
        case Point(x=0, y=0):
            print("Origin is the point's location.")
        case Point(x=0, y=y):
            print(f"Y={y} and the point is on the y-axis.")
        case Point(x=x, y=0):
            print(f"X={x} and the point is on the x-axis.")
        case Point():
            print("The point is located somewhere else on the plane.")
        case _:
            print("Not a point")


# Patterns with positional parameters
var = 0
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
points = Point(y=var, x=1)


# Nested patterns
match points:
    case []:
        print("No points in the list.")
    case [Point(0, 0)]:
        print("The origin is the only point in the list.")
    case [Point(x, y)]:
        print(f"A single point {x}, {y} is in the list.")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two points on the Y axis at {y1}, {y2} are in the list.")
    case _:
        print("Something else is found in the list.")

# Guard - if clause to a pattern, known as a “guard”
match point:
    case Point(x, y) if x == y:
        print(f"The point is located on the diagonal Y=X at {x}.")
    case Point(x, y):
        print(f"Point is not on the diagonal.")

# With Named Constants, using Enums


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


color = Color()
match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")


# ----
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
