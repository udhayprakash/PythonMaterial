"""
Iterable: any object which supports for loop over it.
    Ex: Strings, collections

Integer family
    - int
    - long
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
    print ch,

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

# Collections - dictionaries  - iterable
names = {'first': 'udhay', 'second': 'prakash', 'third': 'someone'}
for each_name in names:
    print(each_name)
