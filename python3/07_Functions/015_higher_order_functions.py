#!/usr/bin/python
"""
Purpose: Higher Order functions
    - function which were designed to work on another functions
    - zip, map, filter, reduce
"""

group1 = ('1', '2', '3')
group2 = ('a', 'b', 'c', 'd')

result = list(zip(group1, group2))
print(result)
print(dict(result))
print()

result = list(zip(group2, group1))
print(result)
print(dict(result))
print()

group3 = (True, False)
print(list(zip(group1, group2, group3)))

print(list(
    zip(
        (1, 2, 3),
        (11, 22, 33, 44),
        (111, 222, 333, 444),
    )
))
print()

# --- HOw to make map to work like zip
print(list(
    map(lambda x, y: (x, y), (1, 2, 3), ['a', 'b'])
))
print()


# # ----------------------------
def is_positive(num):
    return True if num >= 0 else False


data = (12, -23.0, 2, -123, -0, 9)

print(list(
    map(is_positive, data)
))

print(list(
    filter(is_positive, data)
))

# ------- reduce()
from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))

print(list(map(lambda x, y: x + y, [1, 2, 3, 4], [1, 2, 3, 4])))
print([1, 2, 3, 4] + [1, 2, 3, 4])

# Assignment: mimick sum() builtin function with reduce/user-defined func
print(
    sum((1, 23, 23, 2))
)
print(
    sum([(1, 2), (3,), (9, 1)], ())
)
print(
    sum([[1, 2], [3, 4]], [])
)

# Caesar Cipher Implementation
print(list(map(lambda ch: ord(ch), 'Python')))
print(list(map(lambda ch: ord(ch) + 3, 'Python')))
print(list(map(lambda ch: chr(ord(ch) + 3), 'Python')))
print(''.join(map(lambda ch: chr(ord(ch) + 3), 'Python')))
