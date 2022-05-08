#!/usr/bin/python3
"""
Purpose:
"""
from dataclasses import dataclass, field
from typing import Any


# @dataclass(init=False)  # defaut is True
@dataclass()
class Rectangle:
    height: float
    width: float = field(default=44)


# @dataclass(init=False)
@dataclass(init=True)
class Square(Rectangle):
    side: float = 33

    # def __post_init__(self):
    #     super().__init__(self.side, self.side)


sq = Square(side=10, height=20, width=30)
print(
    f"""
    {sq.height  =}
    {sq.width   =}
    {sq.side    =}
"""
)

sq = Square(height=20, width=30)
print(
    f"""
    {sq.height  =}
    {sq.width   =}
    {sq.side    =}
"""
)

"""
NOTE:
In general the dataclass-generated __init__() methods don’t need to be called,
since the derived dataclass will take care of initializing all fields of any
base class that is a dataclass itself.

"""


# ================================


@dataclass
class Base:
    x: Any = 15.0
    y: int = 0


@dataclass
class C(Base):
    z: int = 10
    x: int = 15


# generated __init__() for C will look like
# def __init__(self, x: int = 15, y: int = 0, z: int = 10):
