#!/usr/bin/python
"""
Purpose: linkedList creation

node1 -> node2  -> node3 , ...

each node:
    |data|address of next node

    n1              n2         n3           n4 
 10|id(n2)     20|id(n2)    30|id(n4)    40|None
"""
__author__ = 'Udhay Prakash'

class LinkedList:
    def __init__(self, data, next_node_add=None):
        self.data = data 
        self.next_node_address = next_node_add

    def __repr__(self):
        # return f'''data             : {self.data} \nnext node address: {self.next_node_address}'''
        return f'{self.data}|{self.next_node_address}'

    def get_data(self):
        return self.data 

    def get_next_node_address(self):
        return self.next_node_address

    def change_data(self, new_data):
        self.data = new_data

    def set_next_node_address(self, next_node_address):
        self.next_node_address = next_node_address

n1 = LinkedList(10)
# print(f'n1:{n1}')

n2 = LinkedList(20)
# print(f'n2:{n2}')

n3 = LinkedList(30)

n4 = LinkedList(40)

n1.set_next_node_address(id(n2))
n2.set_next_node_address(id(n3))
n3.set_next_node_address(id(n4))


print(f'n1:{n1}')
print(f'n2:{n2}')
print(f'n3:{n3}')
print(f'n4:{n4}')
print('\n\n\n\n')


# create a linked list for word 'hello'
'''
h|id()     e      l      l    o

'''
list_of_nodes = []
for _index, ech_chr in enumerate('hello'):
    # new node creation
    node = LinkedList(ech_chr, None)
    list_of_nodes.append(node)

    # update address for previous node 
    if _index != 0:
        list_of_nodes[_index -1].set_next_node_address(id(node))

print(list_of_nodes)
