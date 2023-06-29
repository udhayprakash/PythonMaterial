"""
Purpose: Operator Overloading
"""

# Arithmetic  Addition
print(12 + 34)
print(12.0 + 34)
print(12.0 + 234234234234234)
print((3 + 3j) + (4 + 7j))
print()

# string concatenation
print("12" + "34")
print("Python" + " " + "World")
print()

# List concatenation
print([12, 24, 35] + [23, 34])
print()

# (99, 45) + [33, 999]
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'list'

# tuple concatenation
print((99, 45) + tuple([33, 999]))
print((99, 45) + (33, 999))

# print({12, 34, 5} + {2, 5})  # sets doesn't support
# print({'a': 1} + {'c': 4})  # dicts doesn't support
