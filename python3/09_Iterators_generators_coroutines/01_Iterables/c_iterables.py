"""
Purpose:

    bool()
        int
            zero     - False
            non-zero - True
        str
            empty str - False
            non-empty - True
        brace
            empty     - False
            with ele  - True
all() -> True if bool(ech_element) is True
any() -> True if bool(atleast one element) is True
"""

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
'''

# all()
my_list = [1, 2, 3, 4, 6, 0]
for i in my_list:
    if not bool(i):
        result = False
        break
else:
    result = True
print(my_list, result)
print(my_list, all(my_list))

# any()
print()
my_list = [1, 2, 3, 4, 6, 0]
for i in my_list:
    if bool(i):
        result = True
        break
else:
    result = False
print(my_list, result)
print(my_list, any(my_list))

# ------------------
# list
print()
print(all([1, 2, 3, 4, 6]))  # True
print(any([1, 2, 3, 4, 6]))  # True

print()
print(all([1, 1, 1, 0]))     # False
print(any([1, 0, 0, 0]))     # True

print(all([None, 1, 2, 3]))  # False

