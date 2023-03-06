#!/usr/bin/python3
"""
Purpose: Partial functions
"""
import functools


# ordinary function
def multiply(x, y):
    return x * y


print(multiply(2, 4))
print(multiply(2, 14))
print(multiply(2, 2))

# -------------------------------------------
multiply_2 = functools.partial(multiply, 2)
print(f"multiply_2      :{multiply_2}")
print(f"type(multiply_2):{type(multiply_2)}")

assert multiply_2(4) == multiply(2, 4)
assert multiply_2(14) == multiply(2, 14)

assert multiply_2.func == multiply
assert multiply_2.args == (2,)

# ---------
print(multiply(12, 4))
print(multiply(22, 4))
print(multiply(32, 4))

multiply_4 = functools.partial(multiply, y=4)
assert multiply(12, 4) == multiply_4(12)
assert multiply(22, 4) == multiply_4(22)
assert multiply(32, 4) == multiply_4(32)

print(f"{multiply_4.func     =}")
print(f"{multiply_4.args     =}")
print(f"{multiply_4.keywords =}")

"""
Assignments
------------
1) Develop a calculator software which does +, -, *, / operations
    Then, make use of partial functions to optimize your solution.
"""
# ----------------------------------------------
basetwo = functools.partial(int, base=2)
basetwo.__doc__ = "Convert base 2 string to an int."

assert int("10010", base=2) == basetwo("10010")

bin_func = functools.partial(bin)
bin_func.__doc__ = "Convert an int to base 2 string."

print(bin_func(18))
assert bin(18) == bin_func(18)
