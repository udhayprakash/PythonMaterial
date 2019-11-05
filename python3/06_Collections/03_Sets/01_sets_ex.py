#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Properties of sets
    - can't store duplicates
    - sets are unordered
    - can't be indexed
    - stores only immutable object - basic types, tuple, string
    - sets are mutable objects
"""
running_ports = [11, 22, 11, 44, 22, 11]
print('type(running_ports)', type(running_ports))
print('len(running_ports) ', len(running_ports))
print('running_ports      ', running_ports)
print()

myset = {11, 22, 11, 44, 22, 11}
print('type(myset)        ', type(myset))
print('len(myset)         ', len(myset))
print('myset              ', myset)
print()

# sets can't be indexed
# print(myset[0])  # TypeError: 'set' object does not support indexing

filtered_list = list(set(running_ports))
print('type(filtered_list)', type(filtered_list))
print('len(filtered_list) ', len(filtered_list))
print('filtered_list:     ', filtered_list)
print()

print('before addition - myset', myset)
myset.add(12)
print('after addition  - myset', myset)
myset.add(12)
print('after addition  - myset', myset)
myset.add((12,))
print('after addition  - myset', myset)
print()
# myset.update(22) # TypeErroOut: {11, 12, 22, 44}r: 'int' object is not iterable
myset.update('22')
myset.update([12, 34])
print(myset)
print()
myset.update((12, 34, (23, 8)))
print(myset)

# myset.update((99, [11, 11])) # TypeError: unhashable type: 'list'
# myset.update((99, {11, 11})) # TypeError: unhashable type: 'set'
myset.update((99, frozenset({11, 11})))
print(myset)

print()
myset.update('tomato')
print(myset)

print()
myset.update(('tomato',))
print(myset)

print()
myset.add('soap')
print(myset)

print()
myset.update(['tomato', 'ASa'])
print(myset)

print()
# myset.add(['tomato', 'ASa'])
myset.add(('tomato', 'ASa'))
print(myset)

print()
myset.add(('ASa', 'tomato'))
print(myset)

# myset.add(['1', '2'])TypeError: unhashable type: 'list'

myset.add(tuple(['1', '2']))
