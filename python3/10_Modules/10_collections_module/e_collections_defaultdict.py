#!/usr/bin/python
"""
Purpose: Inverting a dictionary 
"""

from collections import defaultdict
from pprint import pprint

alphabets = {'a': 1, 'b': 2, 'c': 3}

inverse_alphabets = defaultdict(None)  # list
for each_char in alphabets:
    # inverse_alphabets[alphabets[each_char]].append(each_char)
    inverse_alphabets[alphabets[each_char]] = each_char

pprint(alphabets)
pprint(inverse_alphabets)

inverse_alph = {v: k for k, v in alphabets.items()}
pprint(inverse_alphabets)
