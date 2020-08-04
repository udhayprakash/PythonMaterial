#!/usr/bin/python3
"""
Purpose: COPY PROBLEM
    assignment vs Shallow copy vs deep copy

Detailed Explanation: https://www.youtube.com/watch?v=yjYIyydmrc0
"""
par_list = [11, 111, 1111]
print('par_list      ', par_list, type(par_list), id(par_list))

hard_copy_list = par_list
print('hard_copy_list', hard_copy_list, type(hard_copy_list), id(par_list))

print('par_list[2]   ', par_list[2])

par_list[2] = 3333  # Substitution
print('par_list[2]   ', par_list[2])
print('par_list      ', par_list, type(par_list))

# leakage problem
print('hard_copy_list', hard_copy_list, type(hard_copy_list))

print()
import copy

# shallow copy
soft_copy_list = copy.copy(par_list)
print('soft_copy_list ', soft_copy_list, type(soft_copy_list), id(soft_copy_list))

print('hard_copy_list[2]', hard_copy_list[2])

hard_copy_list[2] = "FOUR"

print()
print('par_list       ', par_list, type(par_list), id(par_list))
print('hard_copy_list ', hard_copy_list, type(hard_copy_list), id(hard_copy_list))
print('soft_copy_list ', soft_copy_list, type(soft_copy_list), id(soft_copy_list))
print()

print('soft_copy_list[0]', soft_copy_list[0])

soft_copy_list[0] = 'ZERO'
print()
print('par_list       ', par_list, type(par_list), id(par_list))
print('hard_copy_list ', hard_copy_list, type(hard_copy_list), id(hard_copy_list))
print('soft_copy_list ', soft_copy_list, type(soft_copy_list), id(soft_copy_list))

print('='* 60)

new_list = [90, 89, [78, 89, [4, 441, 6]]]
new_softcopy_list = copy.copy(new_list) # soft copy or shallow copy
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

# NOTE: 
# 1. soft(shallow) copy is fast, but cant work more than one dimension
# 2. deep copy is slow, but can work with objects of any number of dimensions
'''
In [1]: l1 = [12, 34]

In [2]: l2 = l1[::]  # soft(shallow) copy

In [3]: id(l1), id(l2)
Out[3]: (95491656, 95452232)

In [4]: l3 = [12, 34, [44, [55]]]

In [5]: l4 = l3[::]

In [6]: id(l3), id(l4)
Out[6]: (80939336, 81194632)

In [10]: l3[2][1][0] = 'five'

In [11]: l3
Out[11]: [12, 34, [44, ['five']]]

In [12]: l4
Out[12]: [12, 34, [44, ['five']]]
'''

'''
Assignment 
----------
1) implement the stack mechanism - LIFO
Take the values in run time
   1. push   - add an element
   2. pop    - delete last element
   3. status - stack size
   
-       -
|       |
|       |
---------
HINT: list.pop(), list.append(), len()

2) implement the queue mechanism - FIFO
Take the values in run time
   1. push   - add an element
   2. pop    - delete last element
   3. status - queue size
    --------
 ->         ->
    --------
HINT: list.insert(), list.pop(), len()
'''
