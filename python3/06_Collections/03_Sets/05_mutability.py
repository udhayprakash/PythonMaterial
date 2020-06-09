#!/usr/bin/python 
"""
Purpose: Sets
        - Sets are mutable
        - Sets cant store mutable objects
        - So, sets cant be stored in sets 
"""
ordinary_set = {11, 22, 33, 22}
print(f'{id(ordinary_set)} {type(ordinary_set)} {ordinary_set}')

# As indexing is not possible, same goes with
#  substitution

ordinary_set.add(99)
print(f'{id(ordinary_set)} {type(ordinary_set)} {ordinary_set}')

# Conclusion - In object changes are possible - so, mutable object

print('\n Frozenset is immutable')
fz_set = frozenset({11, 22, 33, 22})
print(f'{id(fz_set)} {type(fz_set)} {fz_set}')

try:
    fz_set.add(99)
except AttributeError:
    print('frozenset dont have set editable attributes')


print(dir(ordinary_set))
print()
print(dir(fz_set))

try:
    new_set = {1, 2, {2, 3}}
except TypeError:
    print('sets cant be stored in sets - As sets are mutable ')

new_set = {1, 2, frozenset({2, 3})}
print(f'{new_set =}')
# NOTE: frozenset can be stored in sets - As frozenset is immutable