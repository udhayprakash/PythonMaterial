#!/usr/bin/python
"""
Purpose: Binary Search Tree
"""


class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, node):
        self.root = node

    def size(self):
        if self.root is None:
            return 0

        def sub_tree_size(node):
            return 1 + sum(sub_tree_size(c) for c in node.get_children())

        return sub_tree_size(self.root)


class BinaryNode:
    def __init__(self, v):
        self.val = v
        self.leftChild = None
        self.rightChild = None

    def get(self):
        return self.val

    def set(self, v):
        self.val = v

    def get_children(self):
        children = []
        if self.leftChild:
            children.append(self.leftChild)
        if self.rightChild:
            children.append(self.rightChild)
        return children


class BinarySearchTree(Tree):
    def insert(self, val):
        if self.root is None:
            self.set_root(BinaryNode(val))
        else:
            current_root = self.root
            while True:
                if val <= current_root.get():
                    if current_root.leftChild:
                        current_root = current_root.leftChild
                    else:
                        current_root.leftChild = BinaryNode(val)
                        break
                else:
                    if current_root.rightChild:
                        current_root = current_root.rightChild
                    else:
                        current_root.rightChild = BinaryNode(val)
                        break

    def find(self, val):
        current_root = self.root
        while current_root and current_root.get() != val:
            if val < current_root.get():
                current_root = current_root.leftChild
            else:
                current_root = current_root.rightChild

        if current_root is None:
            return False
        else:
            return True


if __name__ == "__main__":
    btree = BinarySearchTree()
    vals = [5, 3, 9, 4, 1, 7, 30]
    for val in vals:
        btree.insert(val)
    print("Tree size is %i" % btree.size())
    tests = [8, 7, 1, 5]
    for t in tests:
        print("find(%i) = %s" % (t, ("True" if btree.find(t) else "False")))
