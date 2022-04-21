#!/usr/bin/python3
"""
Purpose: breakpoint hook
    - sys.breakpointhook
        - Gets called when breakpoint is called
        - works only with builtin breakpoint() function
        - Doesnt work with pdb/ipdb modules
"""
import sys

def hello():
    print('Breakpoint got activated')

sys.breakpointhook = hello


numbers = range(0, 15)

breakpoint()
# import pdb;pdb.set_trace()
# import ipdb;ipdb.set_trace()

for each_num in numbers:
    if each_num % 2 == 0:
        print(each_num, end=' ')
