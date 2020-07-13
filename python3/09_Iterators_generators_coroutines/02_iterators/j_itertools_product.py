#!/usr/bin/python
"""
Purpose: Itertools.product
"""
import itertools

list1 = range(1, 3)
list2 = range(4, 6)
list3 = range(7, 9)

# Method 1
result1 = []
for item1 in list1:
    for item2 in list2:
        for item3 in list3:
            result1.append(item1 + item2 + item3)

# Method 2
result2 = []
for i1, i2, i3 in itertools.product(list1, list2, list3):
    result2.append(i1 + i2 + i3)

assert result1 == result2
