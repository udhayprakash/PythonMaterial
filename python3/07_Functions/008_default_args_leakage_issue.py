#!/usr/bin/python
"""
Purpose: Functions Demo

Memory leakage when mutable objects are taken as 
default arguments
"""

def extend_list(val, my_list=[]):
    my_list.append(val)
    return my_list

list1 = extend_list(123, [])
print(f'list1:{list1}') # [123]

list2 = extend_list(10)
print(f'list2:{list2}') # [10]

list3 = extend_list('a')
print(f'list3:{list3}') # [10, 'a']

print(f'id(list1):{id(list1)}')
print(f'id(list2):{id(list2)}')
print(f'id(list3):{id(list3)}')


print('\n\nSolution when you need default list ==========')
def extend_list(val, my_list=None):
    if not my_list: # my_list == None
        my_list = []
    my_list.append(val)
    return my_list

list1 = extend_list(123, [])
print(f'list1:{list1}') # [123]

list2 = extend_list(10)
print(f'list2:{list2}') # [10]

list3 = extend_list('a')
print(f'list3:{list3}') # [10, 'a']

print(f'id(list1):{id(list1)}')
print(f'id(list2):{id(list2)}')
print(f'id(list3):{id(list3)}')