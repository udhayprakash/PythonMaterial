#!/usr/bin/python
"""
Purpose: linkedList creation

node1 -> node2  -> node3 , ...

each node:
    |data|address of next node

    n1              n2         n3           n4
 10|id(n2)     20|id(n2)    30|id(n4)    40|None
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
            self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        """Inserting at the Beginning"""
        node.next = self.head
        self.head = node

    def add_last(self, node):
        """Inserting at the End"""
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)


if __name__ == "__main__":
    llist = LinkedList(["a", "b", "c", "d"])
    print(llist)  # a -> b -> c -> d -> None

    # llist.add_last(Node("e"))
    # print(llist)  # a -> b -> c -> d -> e -> None

    # llist.add_last(Node("f"))
    # print(llist)  # a -> b -> c -> d -> e -> f -> None

    # # Traverse a Linked List
    # for node in llist:
    #     print(node)

    # print()
    # llist.add_after("a", Node("b"))
    # print(llist)
