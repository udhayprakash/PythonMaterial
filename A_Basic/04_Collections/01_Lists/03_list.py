#!/usr/bin/python
# -*- coding: utf-8 -*-

mylist1 = [1, 11, 111, 1111]
print 'mylist1       = ', mylist1
print 'type(mylist1) = ', type(mylist1)
print

mylist2 = [2, 22, 222, 2222]
print 'mylist2       = ', mylist2
print 'type(mylist2) = ', type(mylist2)
print

newlist = mylist1 + mylist2
print 'newlist       = ', newlist
print 'type(newlist) = ', type(newlist)
print

print 'mylist1.count(11):', mylist1.count(11)
print 'mylist1.count(2) :', mylist1.count(2)

print '=====mylist1.extend(mylist2)====='
mylist1.extend(mylist2)
print 'mylist1       = ', mylist1

print '=== reinitializing the list ==='
mylist1 = [1, 11, 111, 1111]

print '=====mylist1.append(mylist2)====='
mylist1.append(mylist2)
print 'mylist1       = ', mylist1

print '--- mylist1.append(9999)'
mylist1.append(9999)
print 'mylist1       = ', mylist1

# Error --- extend can't take single element
# print '--- mylist1.extend(9999)'
# mylist1.extend(9999)
# print 'mylist1       = ', mylist1


