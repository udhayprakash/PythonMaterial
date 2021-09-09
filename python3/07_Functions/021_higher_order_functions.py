#!/usr/bin/python3
"""
Purpose: Higher Order functions
    - function which were designed to work on another functions
    - zip, map, filter, reduce
    - NOTE: zip(), map() & filter() will ignore the asymmetric values in iterables
"""

group1 = ('1', '2', '3')
group2 = ('a', 'b', 'c', 'd')

result = list(zip(group1, group2))
# NOTE: asymetric values will be ignored
print(result)
print(dict(result))
print()

result = zip(group2, group1)
print(dict(result))
print()

group3 = (True, False)
print(list(zip(group1, group2, group3)))
# print(dict(zip(group1, group2, group3)))
# ValueError: dictionary update sequence element #0 has length 3; 2 is required


print(list(
    zip(
        (1, 2, 3),
        (11, 22, 33, 44),
        (111, 222, 333, 444),
    )
))
print()

# Question: How to make map to work like zip
print(list(
    zip((1, 2, 3), ['a', 'b'])
))
print(list(
    map(lambda x, y: (x, y), (1, 2, 3), ['a', 'b'])
))

# ----------------------------


def is_positive(num):
    return True if num >= 0 else False


data = (12, -23.0, 2, -123, -0, 9)

print(list(
    map(is_positive, data)
))

print(list(
    filter(is_positive, data)
))
print()

# ----------------------------------------
# Caesar Cipher Implementation
print(list(
    map(lambda ch: ch, 'Python')
))
print(list(
    map(lambda ch: ord(ch), 'Python')
))
print(list(
    map(lambda ch: ord(ch)+3, 'Python')
))
print(list(
    map(lambda ch: chr(ord(ch)+3), 'Python')
))
print(
    ''.join(map(lambda ch: chr(ord(ch)+3), 'Python'))
)
