#!/usr/bin/python
# -*- coding: utf-8 -*-

mylist1 = [1, 11, 111, [11]]
print('mylist1       = ', mylist1)

# append, extend, insert
mylist1.append(12)
mylist1.append([23, 34])
print('mylist1       = ', mylist1)

# mylist1.extend(45) # TypeError: 'int' object is not iterable
mylist1.extend('45')
mylist1.extend((56, 78))
print('mylist1       = ', mylist1)

mylist1.insert(0, 99)
mylist1.insert(4, {1, 2})
print('mylist1       = ', mylist1)

print()
# Q: make insert to work like append
# mylist1.insert(-1, 12)
# mylist1.insert(-1, [23, 34])
mylist1.insert(len(mylist1), 12)
mylist1.insert(len(mylist1), [23, 34])
print('mylist1       = ', mylist1)

# ==== deleting with index
print('mylist1[3]    =', mylist1[3])
del mylist1[3]
print('mylist1       = ', mylist1)

print('mylist1[2:6:1]=', mylist1[2:6:1])
del mylist1[2:6:1]
print('mylist1       = ', mylist1)

print()
print('mylist1[1:9:2]=', mylist1[1:9:2])
del mylist1[1:9:2]
print('mylist1       = ', mylist1)

# deleting without index
print()
print('mylist1.pop()', mylist1.pop())
print('mylist1.pop()', mylist1.pop())
print('mylist1       = ', mylist1)

# deleting by element
mylist1 = [11,  [22], 22, 33, 22]
mylist1.remove(22)  # first occurence will be deleted
print('mylist1       = ', mylist1)

# mylist1.remove('q') # ValueError: list.remove(x): x not in list

print()
mylist1.clear()
print('mylist1       = ', mylist1)

del mylist1
print('mylist1       = ', mylist1)
