#!/usr/bin/python
"""
Purpose: Inverting a dictionary 
"""

from collections import defaultdict
from pprint import pprint

alphabets = {'a':1, 'b':2, 'c':3}

inverse_alphabets = defaultdict() #list
for each_char in alphabets:
    # inverse_alphabets[alphabets[each_char]].append(each_char)
    inverse_alphabets[alphabets[each_char]]=each_char

pprint(alphabets)
pprint(inverse_alphabets)
