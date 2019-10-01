"""
Iterable: any object which supports for loop over it.
    Ex:  string, list, tuple, dictionary, set, frozenset, range

NON_Iterable: 
Integer family
    - int
    - float

    - complex
    - boolean

None
bool
"""

# int
# for i in 2:
#     print(i)  # TypeError: 'int' object is not iterable

# for i in None:
#     print i # TypeError: 'NoneType' object is not iterable

# string   -- iterable
for ch in 'python programming':
    print(ch, end=' ')
print()

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
    print(f'each_key:{each_key}\t\teach_val:{each_val}')


print(list('Python Programming'))
print(tuple('Python Programming'))
print(set('Python Programming'))