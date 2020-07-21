#!/usr/bin/python
"""
Purpose: Type Annotation
"""
from typing import List

# created a custom type and aliases to use it
Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(f'new_vector:{new_vector}')
