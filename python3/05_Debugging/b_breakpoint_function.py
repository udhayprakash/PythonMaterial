#!/usr/bin/python
"""
Purpose: Debugging

TASK - To display all even numbers between 0 & 100

NOTE:
    ;(semi-colon) is statement separator
    breakpoint()
        - builtin function, introducted in python 3.6
        - same as import pdb; pdb.set_trace()
"""

numbers = range(0, 100)

# import pdb; pdb.set_trace()
breakpoint()

# To Display all even numbers
for each_num in numbers:
    if each_num % 2 == 0:  # each_num % 2
        print(each_num, end=", ")


# Post Analysis

# python -i SCRIPTNAME.py


# b 21
# b 23
# b 22

# cl 2  -> line 23
# cl 3 -> line 22
