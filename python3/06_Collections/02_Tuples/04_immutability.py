#!/usr/bin/python3
"""
Purpose: Tuples are immutable
            - They doesnt support in-object changes
"""

mytuple = (1, 2, 3)
print('mytuple', mytuple, id(mytuple))

#  Indexing
print(f'{mytuple[2] =}')

# updating an element in tuple
try:
    mytuple[2] = '2.2222'
except TypeError as ex:
    print(ex)
    print('tuple objects are not editable')

# Overwriting
print('\noverwriting (re-assigning)')
mytuple = (1, '2.2222', 3)
print('mytuple', mytuple, id(mytuple))
