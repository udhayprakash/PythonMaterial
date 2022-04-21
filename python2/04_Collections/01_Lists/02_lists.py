#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
List can be classified as single-­dimensional and multi­-dimensional.
List is representing using [].
List is a mutable object, which means elements in list can be changed.
It can store asymmetric data types
"""

numbers = [88, 99, 666]
# homogenous
print 'type(numbers)', type(numbers)
print 'dir(numbers)=', dir(numbers)


print 'len(numbers)=', len(numbers)
print 'numbers.__len__()=', numbers.__len__()
print len(numbers) == numbers.__len__()  # True

print 'str(numbers)           =', str(numbers)
print 'type(str(numbers))     =', type(str(numbers))
print 'numbers.__str__()      =', numbers.__str__()
print 'type(numbers.__str__())=', type(numbers.__str__())

# print "help(numbers)=", help(numbers)
print 'numbers.__doc__=', numbers.__doc__

print 'numbers * 3         =', numbers * 3  # original object not modified
print 'numbers             =', numbers
print 'numbers.__imul__(3) =', numbers.__imul__(3)  # original object IS modified
print 'numbers             =', numbers

print 'id(numbers)=', id(numbers)
# object overwriting
numbers = [88, 99, 666]
print 'id(numbers)=', id(numbers)

# list concatenation
print 'numbers\t\t\t\t=', numbers
alphabets = ['b', 'c']
print 'numbers + alphabets\t\t=', numbers + alphabets
print 'numbers\t\t\t\t=', numbers

print 'numbers.__add__(alphabets)\t=', numbers.__add__(alphabets)
print 'numbers\t\t\t\t=', numbers
# list concatenation will create new obect;
# orginal objects are not changed

print 'numbers.__iadd__(alphabets)\t=', numbers.__iadd__(alphabets)
print 'numbers\t\t\t\t=', numbers  # first object IS changed

print 'numbers.__contains__(12) =', numbers.__contains__(12)
print '12 in numbers =', 12 in numbers

print numbers.__sizeof__()
# # print help(numbers.__sizeof__())
