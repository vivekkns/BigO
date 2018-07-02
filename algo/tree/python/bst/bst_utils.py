from __future__ import print_function
from tree.python.binary_tree_problems import traversals


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


def print_bst():
    btree = """
                10
            /      \\
           7        12
        /  \       /   \\
       2    9     11   13
     /     /
    -6    8
"""
    print(btree)


def bst_insert(root, node):
    if root is None:
        return node

    if node.data <= root.data:
        root.left = bst_insert(root.left, node)
    elif node.data > root.data:
        root.right = bst_insert(root.right, node)
    return root


def get_bst(nodeT=Node):
    root = None
    root = bst_insert(root, nodeT(10))
    root = bst_insert(root, nodeT(12))
    root = bst_insert(root, nodeT(11))
    root = bst_insert(root, nodeT(13))
    root = bst_insert(root, nodeT(7))
    root = bst_insert(root, nodeT(2))
    root = bst_insert(root, nodeT(9))
    root = bst_insert(root, nodeT(8))
    root = bst_insert(root, nodeT(-6))
    return root

if __name__ == '__main__':
    traversals.print_in_order(get_bst())