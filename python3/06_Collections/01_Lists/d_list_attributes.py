#!/usr/bin/python3
# -*- coding: utf-8 -*-

mylist1 = [1, 11, 111, [11]]
print('mylist1       = ', mylist1)

mylist2 = [2, 22, 222]
print('mylist2       = ', mylist2)
print()

# list concatenation
newlist = mylist1 + mylist2
print('newlist       = ', newlist)
print('type(newlist) = ', type(newlist))
print()

print('commutative prop :', mylist1 + mylist2 == mylist2 + mylist1)
print('mylist1 + mylist2', mylist1 + mylist2)
print('mylist2 + mylist1', mylist2 + mylist1)

# Assignment: List repetition is commutative

# print(dir(mylist1))
for each_attribute in dir(mylist1):
    if not each_attribute.startswith('__'):
        print(each_attribute, end=',')
print()

print(f'{mylist1             =}')
print(f'{mylist1.count(2)   =}')
print(f'{mylist1.count(11)   =}')
print(f'{mylist1.count([11]) =}')
# print(f'{mylist1[2].count(11)   =}')
# AttributeError: 'int' object has no attribute 'count'

print(f'{mylist1[3].count(11)   =}')
print(f'{mylist1[3].count([11]) =}')
