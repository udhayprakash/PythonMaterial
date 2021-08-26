#!/usr/bin/python
"""
Purpose: working on comprehensions for 
    list, tuple, set, dictionary
"""
# Traditional
new_list = []
for i in range(2, 9):
    new_list.append(i)
print(new_list)

# List comprehension
other_list = [i for i in range(2, 9)]
print(other_list)

# ---- comprehensions with conditions
even_list = []
for i in range(2, 9):
    if i % 2 == 0:
        even_list.append(i)
print(even_list)

even_list2 = [i for i in range(2, 9) if i % 2 == 0]
print(even_list2)
print()
# ---- comprehensions with if and else
even_or_odd = []
for i in range(2, 9):
    if i % 2 == 0:
        even_or_odd.append('even')
    else:
        even_or_odd.append('odd')
print(even_or_odd)

# Duck-typing

# Ternary operation
print('odd' if True else 'even')
print('odd' if not True else 'even')
print('odd' if not False else 'even')
print('correct' if 23 % 2 == 0 else 'not correct')
print(1 if 6 % 2 == 0 else 0)

print([i % 2 == 0 for i in range(2, 9)])
print([True if i % 2 == 0 else False for i in range(2, 9)])
print(['even' if i % 2 == 0 else 'odd' for i in range(2, 9)])
print()
#########################################
my_variable = [ch for ch in 'Mangalyan']
print(type(my_variable), my_variable)

my_variable = (ch for ch in 'Mangalyan')
print(type(my_variable), my_variable)

my_variable = {ch for ch in 'Mangalyan'}
print(type(my_variable), my_variable)

my_variable = {ch: ord(ch) for ch in 'Mangalyan'}
print(type(my_variable), my_variable)
#########################################

# Assignment 
# chr(), ord()
print('chr(77) ', chr(77))
print("ord('M')", ord('M'))
# caesar cipher
# a b c d e f ......
# 0 1 2 3 4 5 .......
# +3
# bad -> edg
# ex: attack is planned to happen on next sunday

# HINT : % operation, chr(), ord(), list comprehension