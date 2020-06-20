#!/usr/bin/python
"""
Purpose: Iterables - Objects which support iteration over them

non-iterable objects ====> int, float, None, True, False ..
Iterable objects     ====> str, list, tuple, dict, set, iterator, generator, range()

"""
# for i in 1234:
#     print(i)
# TypeError: 'int' object is not iterable

for i in '1234':
    print(i)

# string   -- iterable
for ch in 'python programming':
    print(ch, end=' ')
print()

print('Collections - Lists  - iterable')
names = ['udhay', 'prakash', 'someone']
for each_name in names:
    print('\t', each_name)

print('Collections - tuples  - iterable')
names = ('udhay', 'prakash', 'someone')
for each_name in names:
    print('\t', each_name)

print('Collections - sets  - iterable')
names = {'udhay', 'prakash', 'someone'}
for each_name in names:
    print('\t', each_name)
# NOTE: iterating over sets may not 
# give the elements in defined sequence.

# -----------
print('\nCollections - dictionaries  - iterable')
names = {'first': 'udhay', 'second': 'prakash', 'third': 'someone'}
for each_name in names:
    print('\t' + each_name)
# NOTE: By default, when iterating over dict, it gives its keys only

print('\nkeys')
for each_name in names.keys():
    print('\t' + each_name)

print('\nvalues')
for each_name in names.values():
    print('\t' + each_name)

print('\nitems')
for each_name in names.items():
    print('\t', each_name)

for each_key, each_val in names.items():
    print('\t', each_key, '====>', each_val)


# --------------------
print(list('Python Prog'))
print(tuple('Python Prog'))
print(set('Python Prog'))

