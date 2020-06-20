#!/usr/bin/python
"""
Purpose: Itertools 
            - This modules works with iterators
"""
import itertools

# print(dir(itertools))

# continuously propagates integers from given value
for i in itertools.count(9):
    if i > 14:
        break
    print(i, end=' ')
print()

for i in itertools.count(-3):
    if i > 14:
        break
    print(i, end=' ')
print()

for i in itertools.count():  # default is 0 
    if i > 14:
        break
    print(i, end=' ')
print()


# ----------------------------------------------
# itertools.cycle() - infinitely iterates over a python 
# iterables, unless we explicitly break out of the loop.

c = 0
for i in itertools.cycle(['Head', 'Tail']):
    if c > 7:
        break
    print(i, end=' ')
    c += 1
print()

for c, i in enumerate(itertools.cycle(['Head', 'Tail'])):
    if c > 7:
        break
    print(i, end=' ')
print()


# itertools.repeat() - This one repeats an object infinitely 
# unless explicitly broken out of.
c = 0
for i in itertools.repeat([1, 2, 3]):
    if c > 7:
        break
    print(i)
    c += 1

# We can also specify the number of times we want 
# it to repeat, as a second argument.

print()
for i in itertools.repeat([1, 2, 3], 4):
    print(i)
