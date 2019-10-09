#!/usr/bin/python
"""
Purpose: Stack creation
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items[0]

    def size(self):
        return len(self.items)


s = Stack()

s.push('Hello world!')
s.push(True)
print
"s.size()", s.size()
print
's.pop() ', s.pop()
print
"s.size()", s.size()
