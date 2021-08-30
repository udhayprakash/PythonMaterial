#!/usr/bin/python3
"""
Purpose: Partial Function

Euclidean Distance is calculated between two points
(0, 0) -> (1, 1)
(0, 0) -> (9, 3)
"""
import math
from functools import partial


def euclidean_distance(point1, point2):
    x1, y1 = point1 
    x2, y2 = point2 
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Method 1
distance1 = euclidean_distance( (0, 0), (1, 1) )
print(f'{distance1 =}')
distance2 = euclidean_distance( (0, 0), (9, 3) )
print(f'{distance2 =}')

# Method 2 - using partial functions

zero_euclid = partial(euclidean_distance, (0, 0))

assert euclidean_distance( (0, 0), (1, 1) ) == zero_euclid( (1, 1))
assert euclidean_distance( (0, 0), (9, 3) ) == zero_euclid( (9, 3))
