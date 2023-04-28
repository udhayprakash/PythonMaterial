#!/usr/bin/python3
"""
Purpose: breakpoint hook
    - sys.breakpointhook
        - Gets called when breakpoint is called
        - works only with builtin breakpoint() function
        - Doesnt work with pdb/ipdb modules
"""
import sys


def my_breakpoint_hook_function():
    print("Breakpoint got activated")
    import ipdb

    ipdb.set_trace()


sys.breakpointhook = my_breakpoint_hook_function

numbers = range(0, 100)

# import pdb;pdb.set_trace()
# import ipdb;ipdb.set_trace()
breakpoint()

for each_num in numbers:
    if each_num % 2 == 0:
        print(each_num, end=" ")
