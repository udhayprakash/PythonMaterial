#!/usr/bin/python
"""
purpose: regular expression  demo 

patterns 
    ^ 
    $
"""

import re 
#  ^  the search should happen at the start of string 
#  $   to search at the end only 

# result = re.search('pyTHon$', "Programming is good in PyTHOn", re.I)
result = re.search('pyTHon$', "PyTHOn Programming is good in ", re.I)

print(result, type(result))
if result:
    print('result.group()', result.group())
    print('result.span()', result.span())
    print('result.start()', result.start())
    print('result.end()', result.end())

