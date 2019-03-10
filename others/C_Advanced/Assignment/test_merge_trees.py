import unittest

from merge_trees import TreeNode, BinaryTree


class TestMergeTrees(unittest.TestCase):
    def test_positive_one(self):
        tree1 = TreeNode(1)
        tree1.left = TreeNode(3)
        tree1.right = TreeNode(2)
        tree1.left.left = TreeNode(5)

        tree2 = TreeNode(2)
        tree2.left = TreeNode(1)
        tree2.left.right = TreeNode(4)
        tree2.right = TreeNode(3)
        tree2.right.right = TreeNode(7)

        soln = BinaryTree()
        self.assertEqual(soln.tree(soln.merge_trees(tree1, tree2)), [3, 4, 5, 4, 5, 7])
        soln.res = []
        self.assertEqual(soln.tree(soln.merge_trees(tree2, tree1)), [5, 5, 8, 8, 14])
