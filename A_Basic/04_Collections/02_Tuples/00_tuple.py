#!/usr/bin/python
# -*- coding: utf-8 -*-

mylist = [12, 34, 5, 6, 8]
print 'type(mylist)', type(mylist)
print 'len(mylist)', len(mylist)

mytuple = (12, 34, 5, 6, 8, (5,))
print 'type(mytuple)',type(mytuple)
print 'len(mytuple)', len(mytuple)


another_tuple = (99,)
print 'type(another_tuple)',type(another_tuple)
print 'len(another_tuple)', len(another_tuple)

empty_tuple = () 
print 'type(empty_tuple)',type(empty_tuple)
print 'len(empty_tuple)', len(empty_tuple)


print 'dir(empty_tuple)\n', dir(empty_tuple)
for each in dir(empty_tuple):
    if not each.startswith('__'):
        print each


print 'mytuple', mytuple
print 'mytuple.count(5):', mytuple.count(5)

mytuple = (12, 34, 5, 6, 8, (5))
print 'mytuple', mytuple
print 'mytuple.count(5):', mytuple.count(5)

print 'mytuple.index(34):', mytuple.index(34)




result = (9,99) + (9,) # tuple concatenation
print 'result', result
