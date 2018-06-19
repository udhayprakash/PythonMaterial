#!/usr/bin/python
"""
named tuples provide 
1. access by index - like normal tuples
2. access by keynaame - like dictionaries
3. using getattr()
"""
from collections import namedtuple
from math import sqrt

# normal tuples
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

# using index referencing
line_length = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print line_length

# named tuples
Point = namedtuple('Point', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

# using correspinding attributes for indexing
line_length = sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2)
print line_length

# named tuples are still backwards compatible with normal tuples
# use tuple unpacking
x1, y1 = pt1

"""
use named tuples instead of tuples anywhere you think 
object notation will make your code more pythonic and more 
easily readable.

"""
