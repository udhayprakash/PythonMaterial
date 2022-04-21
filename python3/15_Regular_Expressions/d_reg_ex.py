#!/usr/bin/python
"""
Purpose: Regular Expressions
"""
import re

target_string = "The Python Programming is good for health"
search_string = 'python'

print(f'{target_string.lower().find(search_string.lower()) =}')
print(f'{search_string.lower() in target_string.lower()    =}')
print()

reg_obj = re.compile(search_string, re.I)  # re.IGNORECASE
print(reg_obj, type(reg_obj))

# result = reg_obj.match(target_string)
# .match can get only at the starting of string

result = reg_obj.search(target_string)
# .search - can get any where in the string, including starting
print(f'{result =}')

if result:
    print(f'result.group():{result.group()}')
    print(f'result.span() :{result.span()}')
    print(f'result.start():{result.start()}')
    print(f'result.end()  :{result.end()}')
else:
    print('NO match found')
