#!/usr/bin/python
"""
Purpose: Type Annotation
"""
from collections import defaultdict
from typing import List, Dict, DefaultDict

# created a custom type and aliases to use it
Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(f"new_vector:{new_vector}")

# ===============================


def char_frequency(givenStr: str) -> Dict[str, int]:
    freq: DefaultDict[str, int] = defaultdict(int)
    for each_chr in givenStr:
        freq.setdefault(each_chr, 0)
        freq[each_chr] += 1
    return freq


print(char_frequency("apple"))
