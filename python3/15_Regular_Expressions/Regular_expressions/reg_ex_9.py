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
#  .   to get any character , except newline 

# result = re.search('...', "Programming is good in PyTHOn")
# result = re.search('...$', "Programming is good in PyTHOn")
result = re.search('^.....', "P2r ogramming is good in PyTHOn")


print(result, type(result))
if result:
    print('result.group()', result.group())
    print('result.span()', result.span())