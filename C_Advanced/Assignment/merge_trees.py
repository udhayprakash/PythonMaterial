class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree(object):
    def merge_trees(self, t1, t2):
        if t1 is not None and t2 is not None:
            t1.val += t2.val
            if t1.left is not None and t2.left is not None:
                self.merge_trees(t1.left, t2.left)
            if t1.right is not None and t2.right is not None:
                self.merge_trees(t1.right, t2.right)
            elif t1.right is None and t2.right is not None:
                t1.right = t2.right
        return t1

    res = []

    def tree(self, result):
        if result is not None:
            self.res.append(result.val)
        if result.left is not None:
            self.tree(result.left)
        if result.right is not None:
            self.tree(result.right)
        return self.res


if __name__ == '__main__':
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
    print soln.tree(soln.merge_trees(tree1, tree2))
    soln.res = []
    print soln.tree(soln.merge_trees(tree2, tree1))
