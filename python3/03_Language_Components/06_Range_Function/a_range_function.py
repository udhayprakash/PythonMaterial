#!/usr/bin/python
"""
Purpose: range() function
    - built-in function
    - Used for sequence generation
    - SYNTAX
        range(INITIAL_VALUE, FINAL_VALUE, STEP)
    - Defaults
        INITIAL_VALUE = 0
        STEP = +1
    - FINAL_VALUE is mandatory
    - To get the values,
        - either convert to any iterable -list, tuple or set
        - or, for loop over that object
"""


# values = range()
# TypeError: range expected 1 argument, got 0

values = range(9)  # range(FINAL_VALUE) => range(0, 9, 1)
print(type(values), values)  # <class 'range'> range(0,9)

values = range(0, 9)  # range(INITIAL_VALUE, FINAL_VALUE) => range(0, 9, 1)
print(type(values), values)  # <class 'range'> range(0,9)

values = range(0, 9, 1)  # range(INITIAL_VALUE, FINAL_VALUE, SETP) => range(0, 9, 1)
print(type(values), values)  # <class 'range'> range(0,9)

for each in values:
    print(each)

print(list(values))
print(tuple(values))

print()

values2 = range(0, 9, 2)
print(list(values2))  # [0, 2, 4, 6, 8]

values2 = range(0, 9, -1)
print(list(values2))  # []

values2 = range(9, 0, -1)
print(list(values2))  # [9 8 7 6 5 4 3 2 1]

values2 = range(9, -1, -1)
print(list(values2))  # [9 8 7 6 5 4 3 2 1 0]

values2 = range(9, -1, -3)
print(list(values2))  # [9 6 3 0]


# values2 = range(9, -1, -3.0)
# TypeError: 'float' object cannot be interpreted as an integer

# values2 = range(9.5, -1.5, -3)
# TypeError: 'float' object cannot be interpreted as an integer
