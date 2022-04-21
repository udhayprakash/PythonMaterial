#!/usr/bin/python
"""
Purpose: Double Linked List


  h  e  l  l  o
  3  4  6  8  9

            n1     n2   n3
pre_n_add   None   3    4
value       h      e    l    l   o
next_n_add  4      6    8

"""


class DoubleLinkedList:
    def __init__(self, data, prev_nd_addr=None, next_nd_addr=None):
        self.data = data
        self.prev_nd_addr = prev_nd_addr
        self.next_nd_addr = next_nd_addr

    def set_prev_node_address(self, prev_n_add):
        self.prev_nd_addr = prev_n_add

    def set_next_node_address(self, next_n_add):
        self.next_nd_addr = next_n_add

    def __repr__(self):
        return f"{self.prev_nd_addr}|{self.data}|{self.next_nd_addr}"


d1 = DoubleLinkedList(10)
print(d1)

d2 = DoubleLinkedList(20)
print(d2)

d3 = DoubleLinkedList(30)
print(d3)

d1.set_next_node_address(id(d2))
d2.set_prev_node_address(id(d1))

d2.set_next_node_address(id(d3))
d3.set_prev_node_address(id(d2))
print()
print(d1)
print(d2)
print(d3)

# Assignment L create a double linked list for word 'hello'
"""
id()|h|id()     e      l      l    o

"""
