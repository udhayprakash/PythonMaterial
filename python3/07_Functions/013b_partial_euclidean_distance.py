#!/usr/bin/python
"""
Purpose: Partial Function

Euclidean Distance is calculated between two points
(0, 0) -> (1, 1)
(0, 0) -> (9, 3)
"""
import math

from functools import partial
from typing import Tuple


def euclidean_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


zero_euclid = partial(euclidean_distance, (0, 0))

point = (1, 1)
print(zero_euclid(point))

point = (9, 3)
print(zero_euclid(point))
