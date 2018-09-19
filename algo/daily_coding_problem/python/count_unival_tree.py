
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#       0
#      / \
#     1   0
#        / \
#       1   0
#      / \
#     1   1
#


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def count_unival(root, count):
    if root is None:
        return True

    if not count_unival(root.left, count) or \
            not count_unival(root.right, count):
        return False

    if root.left and root.data != root.left.data:
        return False

    if root.right and root.data != root.right.data:
        return False

    count[0] += 1
    return True


if __name__ == '__main__':
    tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    count = [0]
    count_unival(tree, count)
    print(count[0])
