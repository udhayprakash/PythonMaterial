#!/usr/bin/python
"""
Purpose: Debugging with pudb

TASK - To display all even numbers between 0 & 100

To install ipdb,
    pip install -U pudb --user

NOTE: TO make ipdb as the default, when using breakpoint(),
    export PYTHONBREAKPOINT='pudb.set_trace'

"""

numbers = range(0, 100)

# import pudb; pudb.set_trace()
breakpoint()

for each_num in numbers:
    if each_num % 2 == 0:  # each_num % 2
        print(each_num, end=", ")
