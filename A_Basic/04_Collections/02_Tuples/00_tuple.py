#!/usr/bin/python
# -*- coding: utf-8 -*-

mylist = [12, 34, 5, 6, 8]
print 'type(running_ports)', type(mylist)
print 'len(running_ports)', len(mylist)

mytuple = (12, 34, 5, 6, 8, (5,))
print 'type(mytuple)',type(mytuple)
print 'len(mytuple)', len(mytuple)

print
another_tuple = (99.9,)
print 'type(another_tuple)',type(another_tuple)
print 'len(another_tuple)', len(another_tuple)

print 
empty_tuple = () # tuple()
print 'type(empty_tuple)',type(empty_tuple)
print 'len(empty_tuple)', len(empty_tuple)

print
print 'dir(empty_tuple)\n', dir(empty_tuple)
for each in dir(empty_tuple):
    if not each.startswith('__'):
        print each


print 'mytuple', mytuple
print 'mytuple.count(5):', mytuple.count(5)
print
mytuple = (12, 34, 5, 6, 8, (5))
print 'mytuple', mytuple
print 'mytuple.count(5):', mytuple.count(5)

print 'mytuple.index(34):', mytuple.index(34)
print 'mytuple.index(5) :', mytuple.index(5)


result = (9,99) + (9,) # tuple concatenation
print 'result', result

print
# tuples are immutable 
print 'mytuple', mytuple, id(mytuple)
# mytuple[2] = '2.2222' # TypeError: 'tuple' object does not support item assignment

print 'overwriting'
mytuple = (12, 34, '2.2222', 6, 8, (5,))
print 'mytuple', mytuple, id(mytuple)
