#!/usr/bin/python
"""
Purpose: 
    Factory Design Pattern
"""
from collections import defaultdict
from pprint import pprint

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = {}
for name, colour in colours:
    # favourite_colours[name] = favourite_colours.get(name, []) + [colour]
    favourite_colours.setdefault(name, []).append(colour)
pprint(favourite_colours)

#################################################################
favourite_colours = defaultdict(list)
for name, colour in colours:
    favourite_colours[name].append(colour)

pprint(favourite_colours)

#################################################################
favourite_colours = defaultdict(set)
for name, colour in colours:
    favourite_colours[name].add(colour)

pprint(favourite_colours)

#################################################################
words = ['apple', 'ball', 'cat', 'dog', 'cat']
wdict = defaultdict(int)
for word in words:
    wdict[word] += 1

pprint(wdict)

#################################################################
name = 'Bubbles'
mydict = defaultdict(int)
for i in name:
    mydict[i] += 1

pprint(mydict)
#################################################################
other_dict = defaultdict(lambda: 0)
print(other_dict['one']) # 0 
print(other_dict['two']) # 0
pprint(other_dict)  # {'one': 0, 'two': 0}
