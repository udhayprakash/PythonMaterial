#!/usr/bin/python3
"""
Purpose: Regular Expressions

Question: How to make re.search() to find at the end of string only

pattern
    ^   To make to check at the start of string
    $   To make to check at the end of string
"""
import re

result = re.search('pyTHoN', "PyTHOn Programming is good", re.I)
print(f'\nresult:{result}') 

result = re.search('pyTHoN$', "PyTHOn Programming is good", re.I)
print(f'\nresult:{result}')  # None

result = re.search('pyTHoN$', "Programming is good in PyTHOn", re.I)
print(f'\nresult:{result}')

if result:
    print(f'result.group():{result.group()}')
    print(f'result.span() :{result.span()}')
    print(f'result.start():{result.start()}')
    print(f'result.end()  :{result.end()}')
