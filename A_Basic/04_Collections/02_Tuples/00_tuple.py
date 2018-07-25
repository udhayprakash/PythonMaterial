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
print 'len(mytuple)', len(mytuple)

empty_tuple = ()
print 'type(empty_tuple)',type(empty_tuple)
print 'len(empty_tuple)', len(empty_tuple)

print 'mytuple.count(5):', mytuple.count(5)
