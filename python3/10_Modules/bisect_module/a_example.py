#!/usr/bin/python3
"""
Purpose: bisect module

NOTE:
 1. Bisection is effective for searching ranges of values.
 2. For locating specific values, dictionaries are more performant.
"""
import bisect
import heapq

# --------------------------------
fruits = sorted(['Watermelon', 'loquat', 'Apple', 'jujube'], key=str.lower)
print(fruits)  # ['Apple', 'jujube', 'loquat', 'Watermelon']

# inserting an element into sorted list
bisect.insort(fruits, 'Lemon', key=str.lower)
print(fruits)  # ['Apple', 'jujube', 'Lemon', 'loquat', 'Watermelon']

i = bisect.bisect(fruits, 'lime', key=str.lower)
print(i)  # 3
assert fruits[i] != 'lime'
print(fruits[i])  # 'loquat'


# --------------------------------
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


print([grade(score) for score in (33, 99, 77, 70, 89, 90, 100)])
# ['F', 'A', 'C', 'C', 'B', 'A', 'A']


# --------------------------------
class CornBag:
    def __init__(self, quantity):
        self.quantity = quantity

    def __eq__(self, anotherObject):
        return self.quantity == anotherObject.quantity

    def __lt__(self, anotherObject):
        return self.quantity < anotherObject.quantity

    def __repr__(self):
        return '%d' % self.quantity


bag1 = CornBag(5)
bag2 = CornBag(5)
bag3 = CornBag(10)
bag4 = CornBag(20)


# Compare corn bags
print('Is bag1 equals to bag2 in specification(i.e.,in quantity)')
print(bag1 == bag2)
print('Is bag1 is bag2:', bag1 is bag2)

# Create a Python list of corn bags
cornbags = [bag1, bag2, bag4, bag3]
print('Corn bags:', cornbags)

heapq.heapify(cornbags)

# Sort the corn bags
print('Corn bags sorted based on quantity:')
ordered = heapq.nsmallest(len(cornbags), cornbags)
print(ordered)

# Find the insertion points for a bag with a quantity of 10 units of corn
pos = bisect.bisect_right(ordered, CornBag(10))
print('The new entry with an already existing value can be inserted to the right of the value at position:')
print(pos)

pos = bisect.bisect(ordered, CornBag(10))
print(pos)

print('The new entry with an already existing value can be inserted to the left of the value at position:')
pos = bisect.bisect_left(ordered, CornBag(10))
print(pos)
