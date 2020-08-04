#!/usr/bin/python3
"""
Purpose: List referencing problem
"""

my_list1 = []
print(f'{my_list1 =}')  # []

my_list1 = [] * 3
print(f'{my_list1 =}')  # []

# Anti-pattern
my_list1 = [[]] * 3
print(f'{my_list1 =}')  # [[], [], []]

my_list1[0].append(3)
print(f'{my_list1 =}')  # [[3], [3], [3]]
print()
# NOTE: that items in the sequence s are not copied;
#  they are referenced multiple times.

# SOLUTION
my_list2 = [[] for i in range(3)]
print(f'{my_list2 =}')

my_list2[0].append(3)
print(f'{my_list2 =}')

my_list2[2].append(4)
print(f'{my_list2 =}')
print('\n\n')

# Another Example
new_list = [[None] * 2] * 3
print(f'{new_list =}')  # [[None, None], [None, None], [None, None]]

new_list[0][0] = 5
print(f'{new_list =}')  # [[5, None], [5, None], [5, None]]

new_list = [[None] * 2 for i in range(3)]
new_list[0][0] = 5
print(f'{new_list =}')  # [[5, None], [None, None], [None, None]]
