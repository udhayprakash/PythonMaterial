"""
Purpose:

all() -> True if bool(ech_element) is True
any() -> True if bool(atleast one element) is True
"""
print(all([1, 2, 3, 4, 6])) # True
print(any([1, 2, 3, 4, 6])) # True

print(all([1, 1, 1, 0]))    # False
print(any([1, 0, 0, 0]))    # True

print(all([None, 1, 2, 3]))    # False
