#!/usr/bin/python3
"""
Purpose: Set Attributes
"""
# only in Python 2.x , we have sets module
# import sets
# print(dir(sets)) # ModuleNotFoundError: No module named 'sets'
import sys

simple_set = {1, 2, 3}
print(dir(simple_set))
# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__',
#  '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__',
#  '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__',
#  '__str__', '__sub__', '__subclasshook__', '__xor__',
#
#  'add', 'clear', 'copy', 'difference', 'difference_update',
#  'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
#  'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

assert simple_set.__contains__(2) == (2 in simple_set)
assert simple_set.__contains__(6) == (6 in simple_set)
print(f'{6 in simple_set =}')

print(f'\n{simple_set.__sizeof__()   =}')  # python object
print(f'{sys.getsizeof(simple_set) =}')  # Along with c header
print()

print(f'{simple_set.__and__(1) =}')  # NotImplemented
print(f'{simple_set.__and__({1}) =}')  # {1}

# __add__ will not change the original set
print(f'{simple_set =}')

for each_attribute in dir(simple_set):
    if not each_attribute.startswith('__'):
        print(each_attribute)
print()

# list.append/list.insert  <-> set.add
#   :- takes both iterable & non-iterable items
#   :- Can store only immutable objects
print(f'{simple_set =}')

simple_set.add(99)
print(f'{simple_set =}')

simple_set.add(99)
print(f'{simple_set =}')

simple_set.add((99,))
print(f'{simple_set =}')

try:
    simple_set.add([11, 22])
except TypeError:
    print('mutable objects(list, set, dict) cant be stored in set')

try:
    simple_set.add({11, 22})
except TypeError:
    print('mutable objects(list, set, dict) cant be stored in set')

simple_set.add('Python')
print(f'{simple_set =}')

# list.extend  <-> set.update
#   :- Only iterable objects are allowed
#   :- will add to same dimension
print()
simple_set = {1, 2, 3}

try:
    simple_set.update(888)
except TypeError:
    print('Only iterable objects can be used with set.update')

simple_set.update((8, 88))
print(f'{simple_set =}')

simple_set.update([8, 7])
print(f'{simple_set =}')

simple_set.update([8, 7, (2, 3), (9,)])
print(f'{simple_set =}')

try:
    simple_set.update([8, 7, [2, 3]])
except TypeError:
    print('Inner element is a list')
print(f'{simple_set =}')

# Question
try:
    simple_set.update([9, (8, 7, [9])])
except TypeError:
    print('Inner of inner dimension has a list')

# Q) How to remove elements from the set
# Ans) set.pop, set.remove, set.discard

# set.pop() - remove a random value
print()
print(f'{simple_set.pop()}')
print(f'After pop ->{simple_set}')

print(f'{simple_set.pop()}')
print(f'After pop ->{simple_set}')

print(f'{simple_set.pop()}')
print(f'After pop ->{simple_set}')

# set.remove
#   - to remove a specific element
#   - throws KeyError exception if that element is not present
print()
simple_set.remove(8)
print(f'After remove->{simple_set}')

simple_set.remove(7)
print(f'After remove->{simple_set}')

simple_set.remove((2, 3))
print(f'After remove->{simple_set}')

try:
    simple_set.remove('Q')
except KeyError:
    print('That element is not present')

# set.discard
#   - to remove a specific element
#   - No error is thrown when element is not present
print()
simple_set.discard('Q')
print(f'After discard->{simple_set}')

simple_set.discard(88)
print(f'After discard->{simple_set}')

simple_set.discard((99,))
print(f'After discard->{simple_set}')

print()
new_set = simple_set.copy()
print(f'{simple_set =} {id(simple_set) =}')
print(f'{new_set    =} {id(new_set)    =}')

simple_set.clear()
print('\n After simple_set.clear()')
print(f'{simple_set =} {id(simple_set) =}')
print(f'{new_set    =} {id(new_set)    =}')

# Assignment
#  1. Try adding a string to both set.add & set.update &
#  observe the difference
#  'tomoto'
