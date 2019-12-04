#!/usr/bin/python
"""
Purpose:
"""

# iterables
alpha = {'a', 'e', 'i', 'o'}
nums = ('1', '2', '3', '4')

pairs = zip(alpha, nums)
print(f'pairs: {type(pairs)} {pairs}')

# Method 1: Iterate over the object
for ech_pair in pairs:
    print(ech_pair)

# Method 2: Convert to other iterables
pairs1 = list(pairs)
print(f'pairs1: {type(pairs1)} {pairs1}')

pairs2 = tuple(pairs)
print(f'pairs2: {type(pairs2)} {pairs2}')

pairs3 = set(pairs)
print(f'pairs3: {type(pairs3)} {pairs3}')

pairs4 = str(pairs)
print(f'pairs4: {type(pairs4)} {pairs4}')

# Iterators are disposable objects.
# can give values only once
# re-assign to retrieve values again
print()
pairs = zip(alpha, nums)
pairs1 = list(pairs)
print(f'pairs1: {type(pairs1)} {pairs1}')

print()
pairs = zip(alpha, nums)
pairs2 = tuple(pairs)
print(f'pairs2: {type(pairs2)} {pairs2}')

print()
pairs = zip(alpha, nums)
pairs3 = set(pairs)
print(f'pairs3: {type(pairs3)} {pairs3}')

print()
pairs = zip(alpha, nums)
pairs4 = str(pairs) # <zip object at 0x0000000002606688>
print(f'pairs4: {type(pairs4)} {pairs4}')

print()
pairs = zip(alpha, nums)
pairs5 = dict(pairs)
print(f'pairs5: {type(pairs5)} {pairs5}')


# Assignment: repeat above statements for map & filter