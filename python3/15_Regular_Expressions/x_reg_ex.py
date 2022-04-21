#!/usr/bin/python3
"""
purpose: regular expression
"""

import re

p = re.compile("(blue|white|red)")
print(p.match("blue Lorries and red Busses").group())
print(p.search("blue Lorries and red Busses").group())
print(p.findall("blue Lorries and red Busses"))
print()

print(p.sub("colour", "blue Lorries and red Busses"))
print(p.subn("colour", "blue Lorries and red Busses"))
