#!/usr/bin/env python

from math import sqrt
import numarray

def stddev2(numbers):
    n, = numbers.shape
    sum = numarray.sum(numbers)
    sum_of_squares = numarray.sum(numbers * numbers)
    return sqrt(sum_of_squares / n - (sum / n) ** 2)

