#!/usr/bin/python
"""
Purpose: iter() protocol
    Iterator objects
        - iterator is an immutable, disposable and lazy object
        - designed for builtin iterable objects
        - can't be indexed
        - stores the state
        - used for large data handling
        - values can be retrieved by 
            - .next() in python 2.x 
            - .__next__() in python 3.x
            - applying for loop
"""
alpha = ['a', 'e', 'i', 'o', 'u']
print(f'alpha       : {type(alpha)} {alpha}')
print(f'len(alpha)  : {len(alpha)}')
# Indexing
print(f'alpha[2]    : {alpha[2]}')
# slicing
print(f'alpha[2:5]  : {alpha[2:5]}')


alpha_it = iter(alpha)
print(f'alpha_it       : {type(alpha_it)} {alpha_it}')
# print(f'len(alpha_it)  : {len(alpha_it)}') # TypeError: object of type 'list_iterator' has no len()
# print(f'alpha_it[2]    : {alpha_it[2]}') # TypeError: 'list_iterator' object is not subscriptable
# print(f'alpha_it[2:5]  : {alpha_it[2:5]}') # TypeError: 'list_iterator' object is not subscriptable

# Method 1: iterate over the object
for ech_ele in alpha_it:
    print(ech_ele)


# Method 2: Convert to other iterables
print('list(alpha_it)', list(alpha_it))

alpha_it = iter(alpha)
print('list(alpha_it)', list(alpha_it))

alpha_it = iter(alpha)
print('tuple(alpha_it)', tuple(alpha_it))

alpha_it = iter(alpha)
print('set(alpha_it)', set(alpha_it))

alpha_it = iter(alpha)
print('str(alpha_it)', str(alpha_it)) # <list_iterator object at 0x0000000002684188>
