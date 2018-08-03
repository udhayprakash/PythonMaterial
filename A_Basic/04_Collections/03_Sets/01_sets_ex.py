#!/usr/bin/python
# -*- coding: utf-8 -*-

running_ports = [11, 22, 11, 44, 22, 11]
print 'type(running_ports)', type(running_ports)
print 'len(running_ports)', len(running_ports)
print 'running_ports', running_ports
print

myset = {11, 22, 11, 44, 22, 11}
print 'type(myset)', type(myset)
print 'len(myset)', len(myset)
print 'myset', myset
print


# sets can't be indexed
# print myset[0]  # TypeError: 'set' object does not support indexing

filtered_list = list(set(running_ports))
print 'type(filtered_list)', type(filtered_list)
print 'len(filtered_list)', len(filtered_list)
print 'filtered_list:', filtered_list
print 

print myset
print 'myset.add(12)', myset.add(12)
print myset

# myset.update(22) # TypeError: 'int' object is not iterable
myset.update([12, 34])
print myset

myset.update((12, 34, (23, 8)))
print myset

# myset.update((99, [11, 11])) # TypeError: unhashable type: 'list'
# print myset

myset.update('tomato')
print myset

myset.update(['tomato', 'ASa'])
print myset




'''
datatypes
===========
    int()
    long()
    float()
    str()

data Structures
===============
    list()
    tuple()
    set()
    dict()

    iter()
'''






