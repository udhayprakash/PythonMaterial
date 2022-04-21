#!/usr/bin/python
"""
Purpose: Unpacking
    - works when same no. of variables and values
      are present on both sides
"""
num1 = 12
num2 = 34
print(f"num1 = {num1}  num2 = {num2}")

# unpacking
num1, num2 = 12, 34
print(f"num1 = {num1}  num2 = {num2}")

p1, p2, p3, p4, p5 = 99, 88, 66, 77, 44
print(f"p1 = {p1}  p2 = {p2} p3 = {p3} p4 = {p4} p5 = {p5}")

try:
    p1, p2, p3, p4 = 99, 88, 66, 77, 44
except ValueError as ex:
    print(ex)

p = 99, 88, 66, 77, 44
print(f"p={p} type(p)={type(p)}")

# n1, n2 = 1, 2, 3, 4, 5  # ValueError: too many values to unpack (expected 2)

n1, *n2 = 1, 2, 3, 4, 5
print(f"n1={n1} \nn2={n2}")

print()
n1, *n2, n3 = 1, 2, 3, 4, 5
print(f"n1={n1} \nn2={n2} \nn3={n3}")  # n2 is of type list
