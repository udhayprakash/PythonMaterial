#!/usr/bin/python
"""
Purpose: Tuples are immutable
            - They doesnt support in-object changes
"""

mytuple = (1, 2, 3)
print('mytuple', mytuple, id(mytuple))

try:
    mytuple[2] = '2.2222'
except TypeError as ex:
    print(ex)
    print('tuple objects are not editable')

# Overwriting 
print('\noverwriting (re-assigning)')
mytuple = (1,'2.2222', 3)
print('mytuple', mytuple, id(mytuple))
