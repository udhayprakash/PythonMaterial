#!/usr/bin/python3
"""
Purpose:
"""
from collections import ChainMap

alpabets = {'a': 1, 'b': 2, 'c': 3}
fruits = {'a': 'apple', 'b': 'banana'}

# Method 1
combined = alpabets.copy()
combined.update(fruits)
print(combined)  # {'a': 'apple', 'b': 'banana', 'c': 3}

# Method 2
fruit_alphabets = ChainMap(fruits, alpabets)
print(dict(fruit_alphabets))  # {'a': 'apple', 'b': 'banana', 'c': 3}


alpabet_fruits = ChainMap(alpabets, fruits)
print(dict(alpabet_fruits))  # {'a': 1, 'b': 2, 'c': 3}


# --------------
d1 = {'a': 1}
d2 = {'b': 2, 'd': 4}
d3 = {'c': 3}

# Defining the chainmap
c = ChainMap(d1, d2, d3)

print(dir(c))
print(dict(c))  # {'c': 3, 'b': 2, 'd': 4, 'a': 1}
print(c.parents)  # ChainMap({'b': 2, 'd': 4}, {'c': 3})
