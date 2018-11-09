#!/usr/bin/env python
"""
This is matrix geberator for password_generator.

It generates matrix, which should be saved as matrix.py file
in the same directory, where password_generator is saved

"""
import random


def matrix_generate():
    """
    Generate matrix using randomly generated values from defined
    set of chars (ASCII codes from 48 to 122 decimal)
    """
    matrix = {}
    for x in range(48, 122):
        matrix[x] = {}
        for y in range(48, 122):
            matrix[x][y] = chr(random.randint(48, 122))
    return matrix


# print generated matrix
print matrix_generate()
