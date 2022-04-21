#!/usr/bin/python3
"""
Purpose: To prove  that lists are mutable

Mutable objects: List, set, dict
immutable objects: int, float, str, bool, None, tuple, frozenset, iterator
"""

num1 = 1234
print(f'{num1 =} {type(num1)} {id(num1)=}') # 1380925482512

num1 = 9999
print(f'{num1 =} {type(num1)} {id(num1)=}') # 1380925482320

# ------------------------------------------------
print('\nString is a immutable object ===')
name = 'Raj Sekhar'
print(f'name         :{name}')
print(f'name[0:3]    :{name[0:3]}')
# name[0:3] = 'Tej'   # editing is NOT possible
# TypeError: 'str' object does not support item assignment

print('id(name)', id(name))  # 2453918545968
name = 'Tej Sekhar'  # overwriting the object
print('id(name)', id(name))  # 2453918546352
print(name)

# ------------------------------------------------
# multi-dimensional lists
ml = [1, 2, 3, 4.3, 5, [6, 7, 8, (9, 10)]]
#     0  1  2   3   4  --------5--------
#                       0  1  2   --3--
#                                 0   1
print()
print('List is a mutable object =======')
print('ml           ', ml)          # value
print('type(ml)     ', type(ml))    # data type
print('id(ml)       ', id(ml))      # address location - 2184777775552

print(f'{ml[3] = }')  # 4.3

ml[3] = 3.4
print('ml           ', ml)
print('id(ml)       ', id(ml))  # 2184777775552
print()
