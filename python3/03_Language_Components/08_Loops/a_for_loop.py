#!/usr/bin/python 
"""
Purpose: for loop

    Two types of for loops in any language:
        1. for (int a = 0; a < 10 ; a ++)       ==> This is not valid in python
        2. for a in range(0, 10, 1)             ==> This is the only valid for loop in python

NOTE: for loop can be applied only on ITERABLE OBJECT
    non-iterable objects - int, float, None, bool(True/False)
    iterable objects     - string, range, list, tuple, set, dictionary, iterators, generators

"""
# # int
# for i in 12123:
#     print(i)
# TypeError: 'int' object is not iterable

# # float 
# for i in 1233.3123:
#     print(i)
# TypeError: 'float' object is not iterable

# # None
# for i in None:
#     print(i)
# TypeError: 'NoneType' object is not iterable

# # bool - True/False
# for i in True:
#     print(i)
# TypeError: 'bool' object is not iterable

# strings
for i in 'Python':
    # print(i, end='\n')
    print(i, end=', ')
print()

for ch in '12312123':
    print(ch, end=', ')
print()

for each in str(1231.123):
    print(each, end=', ')
print()

for each in str(True):
    print(each, end=', ')
print()

for each in 'None':
    print(each, end=', ')
print()

for each_chr in 'Python':
    print(each_chr)

# enumerate() - builtin function to get the 
#               loop index
for each_chr in enumerate('Python'):
    print(each_chr)

# unpacking
for loop_index, each_chr in enumerate('Python'):
    # print(loop_index, each_chr)
    print(f'At position {loop_index}, character is {each_chr}')
print()

# To get the loop index with an offset
for loop_index, each_chr in enumerate('Python', -3):
    print(f'At position {loop_index}, character is {each_chr}')
print()

for loop_index, each_chr in enumerate('Python', 7):
    print(f'At position {loop_index}, character is {each_chr}')
print()


# lists
for each_ele in [11, 22, 33, 44, 55]:
    print(each_ele, end=', ')
print()

for each_ele in enumerate([11, 22, 33, 44, 55]):
    print(each_ele)
print()

for loop_index, each_ele in enumerate([11, 22, 33, 44, 55]):
    print(f'{loop_index} ===> {each_ele}')
print()

# Assignment: perform for loop & Enumeration on range() object