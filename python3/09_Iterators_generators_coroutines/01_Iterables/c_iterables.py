"""
Purpose:

all() -> True if bool(ech_element) is True
any() -> True if bool(atleast one element) is True
"""
bool()
# list
print(all([1, 2, 3, 4, 6]))  # True
print(any([1, 2, 3, 4, 6]))  # True

print(all([1, 1, 1, 0]))     # False
print(any([1, 0, 0, 0]))     # True

print(all([None, 1, 2, 3]))  # False


'''
>>> bool(1)
True
>>> bool(0)
False
>>>
>>> bool(0.34234)
True
>>> bool(0.000000)
False
>>> bool('aS')
True
>>> bool(' ')
True
>>> bool('')
False
>>>
>>>

'''