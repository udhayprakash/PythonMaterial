#!/usr/bin/python
"""
purpose: regular expression  demo 
"""

import re 

target_string = "The Python Programming is good for health"

search_string = 'pyTHon'

reg_obj = re.compile(search_string, re.I) # re.IGNORECASE


# .match can get only at the starting of string
# result = reg_obj.match(target_string)
result = reg_obj.search(target_string)

print(result, type(result))
if result:
    print('result.group()', result.group())
    print('result.span()', result.span())
    print('result.start()', result.start())
    print('result.end()', result.end())
