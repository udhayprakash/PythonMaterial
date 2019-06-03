#!/usr/bin/python
"""
Purpose: binary tree implementation
    real world uses:
        chess game
        In data science, Decision tree based learning
        XML parsers, ...
"""
class Tree:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left  = left
        self.right = right

    def __str__(self):
        return f'{self.info} , Left child: {self.left} , Right child: {self.right}'

# tree = Tree(1, Tree(2, 2.1, 2.2), Tree(3, 3.1))
# print(tree)

tree1 = Tree(1)
print(tree1)
# print(dir(tree1))
# print('tree1.left', tree1.left)
# print('tree1.right', tree1.right)

print()
tree2 = Tree(2, 2.1, 2.2)
print(tree2)
# print(dir(tree2))
# print('tree2.left', tree2.left)
# print('tree2.right', tree2.right)

tree1.left = tree2
print(tree1)
