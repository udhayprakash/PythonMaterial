#!/usr/bin/python
"""
Purpose: Stack data structure implementation
"""
__author__ = 'Udhay Prakash'


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        poped_item = self.items[0]
        del self.items[0]
        return poped_item

    def size(self):
        return len(self.items)


s = Stack()

s.push('Hello world!')
s.push(True)
print "s.size()", s.size()
print 's.pop() ', s.pop()
print "s.size()", s.size()
