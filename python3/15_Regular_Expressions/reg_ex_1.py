#!/usr/bin/python
"""
purpose: regular expression  demo 
"""

import re 

target_string = "Python Programming is good for health"

search_string = 'Python'

reg_obj = re.compile(search_string)

result = reg_obj.match(target_string)

print(result)
print('result.group()', result.group())
print('result.span()', result.span())
print('result.start()', result.start())
print('result.end()', result.end())
