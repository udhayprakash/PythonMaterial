#!/usr/bin/python
"""
Purpose: COPY PROBLEM
    assignment vs Shallow copy vs deep copy

Detailed Explanation: https://www.youtube.com/watch?v=yjYIyydmrc0
"""

# par_list = [11, 111, 1111]
# print('par_list      ', par_list, type(par_list), id(par_list))

# hard_copy_list = par_list
# print('hard_copy_list', hard_copy_list, type(hard_copy_list), id(par_list))

# print('par_list[2]   ', par_list[2])

# par_list[2] = 3333
# print('par_list[2]   ', par_list[2])
# print('par_list      ', par_list, type(par_list))

# # leakage problem
# print('hard_copy_list', hard_copy_list, type(hard_copy_list))

# print()
import copy

# # shallow copy
# soft_copy_list = copy.copy(par_list)
# print('soft_copy_list ', soft_copy_list, type(soft_copy_list), id(soft_copy_list))


# print('hard_copy_list[2]', hard_copy_list[2])

# hard_copy_list[2] = "FOUR"
# print()
# print('par_list       ', par_list, type(par_list), id(par_list))
# print('hard_copy_list ', hard_copy_list, type(hard_copy_list), id(hard_copy_list))
# print('soft_copy_list ', soft_copy_list, type(soft_copy_list), id(soft_copy_list))

# print('soft_copy_list[0]', soft_copy_list[0])

# soft_copy_list[0] = 'ZERO'
# print()
# print('par_list       ', par_list, type(par_list), id(par_list))
# print('hard_copy_list ', hard_copy_list, type(hard_copy_list), id(hard_copy_list))
# print('soft_copy_list ', soft_copy_list, type(soft_copy_list), id(soft_copy_list))


# print('='* 60)

new_list = [90, 89, [78, 89, [4, 441, 6]]]
new_softcopy_list = copy.copy(new_list)
new_deepcopy_list = copy.deepcopy(new_list)

print('new_list          ', new_list, type(new_list), id(new_list))
print('new_softcopy_list ', new_softcopy_list, type(new_softcopy_list), id(new_softcopy_list))
print('new_deepcopy_list ', new_deepcopy_list, type(new_deepcopy_list), id(new_deepcopy_list))

print('new_list[2][2][1]', new_list[2][2][1])

new_list[2][2][1] = 'FFO'
print()
print('new_list          ', new_list, type(new_list), id(new_list))
print('new_softcopy_list ', new_softcopy_list, type(new_softcopy_list), id(new_softcopy_list))
print('new_deepcopy_list ', new_deepcopy_list, type(new_deepcopy_list), id(new_deepcopy_list))

'''
In [1]: l1 = [12,34]

In [2]: l2 = l1[::]

In [3]: id(l1), id(l2)
Out[3]: (95491656, 95452232)

'''
