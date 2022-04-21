class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))


if __name__ == '__main__':
    circular_llist = CircularLinkedList()
    circular_llist.print_list()  # None

    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    d.next = a
    circular_llist.head = a
    circular_llist.print_list()   # a -> b -> c -> d
    circular_llist.print_list(b)  # b -> c -> d -> a
    circular_llist.print_list(d)  # d -> a -> b -> c
