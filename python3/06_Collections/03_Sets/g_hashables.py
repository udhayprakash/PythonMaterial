#!/usr/bin/python3
"""
Purpose: hash()
"""

assert (123).__hash__() == hash(123)

# my_set = {1, 2, [3,4]}  # TypeError: unhashable type: 'list'
# my_set = {1, 2, {3,4}}  # TypeError: unhashable type: 'set'
# my_set = {1, 2, {3:4}}    # TypeError: unhashable type: 'dict'

my_set = {1, 2, frozenset({3,4})} 
my_set = {1, 2, tuple({3,4})} 
my_set = {1, -0.98798, 23 + 3j, False, None, (1,2), frozenset((3, 4))} 
print(f'{my_set =}')


# data = [1, -0.98798, 23 + 3j, False, None, [1, 2], (1,2), {2, 3}, frozenset((3, 4)), {2:3}]

# for each_data in data:
#     print(f'{hash(each_data)} {type(each_data)} {each_data}' )


# Immutable object 
print(f'{hash(123)              = }')
print(f'{hash(-0.2323)          = }')
print(f'{hash(2 + 3j)           = }')
print(f'{hash(True)             = }')
print(f'{hash(None)             = }')

print(f'{hash((3,4))            = }')

print(f'{hash(frozenset((3,4))) = }')
# Mutable Objects
for each_obj in [ [1,2], {3,4}, {'a': 1} ]:
    try:
        hash(each_obj)
    except TypeError as ex:
        print(each_obj, ex)

# Conclusion 
# 1. hash can be created for immutable objects only 
# so, immutable objects are also called hashable objects
