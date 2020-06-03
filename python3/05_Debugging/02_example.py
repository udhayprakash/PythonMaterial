#!/usr/bin/python
"""
Purpose: Debugging 

TASK - To display all even numbers between 0 & 100

NOTE: 
    ;(semi-colon) is statement separator
    breakpoint() 
        - builtin function 
        - same as import pdb; pdb.set_trace()
"""
numbers = range(0, 100)

# import pdb; pdb.set_trace()
breakpoint()

for each_num in numbers:
    if each_num % 2 == 0:
        print(each_num, end=' ')