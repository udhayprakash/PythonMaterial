#!/usr/bin/python

# Stack Abstract Data Type (ADT) Implementation

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()  # Object Instantiation

print
"s.is_empty() ", s.is_empty()

s.push(1234)
s.push('Python')
print
"s = ", s
print
"s.peek() ", s.peek()
s.push(True)
print
"s.size()", s.size()
print
"s.is_empty() ", s.is_empty()
s.push(23.45)
print
"s.pop() ", s.pop()
print
"s.pop() ", s.pop()
print
"s.size() ", s.size()
