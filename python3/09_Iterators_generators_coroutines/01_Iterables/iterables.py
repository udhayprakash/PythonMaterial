"""
Iterable: any object which supports for loop over it.
    Ex:  string, list, tuple, dictionary, set, frozenset, xrange
Integer family
    - int
    - float

    - complex
    - boolean

Strings

None

Collections
    - Lists
    - Tuples
    - Sets
    - Dictionaries

"""

# int
# for i in 2:
#     print i  # TypeError: 'int' object is not iterable

# string   -- iterable
for ch in 'python programming':
    print(ch, end=',')

# for i in None:
#     print i # TypeError: 'NoneType' object is not iterable

# Collections - Lists  - iterable
names = ['udhay', 'prakash', 'someone']
for each_name in names:
    print(each_name)

# Collections - tuples  - iterable
names = ('udhay', 'prakash', 'someone')
for each_name in names:
    print(each_name)

# Collections - sets  - iterable
names = {'udhay', 'prakash', 'someone'}
for each_name in names:
    print(each_name)

print('\nCollections - dictionaries  - iterable')
names = {'first': 'udhay', 'second': 'prakash', 'third': 'someone'}
for each_name in names:
    print(each_name)

print('\nkeys')
for each_name in names.keys():
    print(each_name)

print('\nvalues')
for each_name in names.values():
    print(each_name)

print('\nitems')
for each_name in names.items():
    print(each_name)

for each_key, each_val in names.items():
    # print('each_key',each_key, 'each_val', each_val)
    print(f'each_key:{each_key} each_val:{each_val}')


for each_chr in enumerate('Python Programming'):
    print(each_chr)


for loop_index, each_chr in enumerate('Python Programming'):
    print(f'In loop {loop_index}, value is {each_chr}')
