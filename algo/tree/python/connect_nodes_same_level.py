from __future__ import print_function
import binary

# Input Tree
#        A
#       / \
#      B   C
#     / \   \
#    D   E   F
#
#
# Output Tree
#       A--->NULL
#      / \
#     B-->C-->NULL
#     / \ \
#    D-->E-->F-->NULL
#


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.Next = None
        self.data = data


def con_same_level(root):
    if root is None:
        return

    if root.left is not None:
        root.left.Next = root.right

    if root.right is not None:
        if root.Next is not None:
            root.right.Next = root.Next.left
        else:
            root.right.Next = None

    con_same_level(root.left)
    con_same_level(root.right)


def get_first_node(node):
    # keep traversing the list till we
    # find a valid node
    while node is not None:
        print(node.data)
        if node.left is not None:
            return node.left
        if node.right is not None:
            return node.right
        node = node.Next
    return None


def con_same_level_incomplete(root):
    if root is None:
        return

    if root.left is not None:
        if root.right is not None:
            root.left.Next = root.right
        else:
            root.left.Next = get_first_node(root.Next)

    if root.right is not None:
        root.right.Next = get_first_node(root.Next)

    con_same_level_incomplete(root.left)
    con_same_level_incomplete(root.right)


def print_level_next_pointer(root):
    if root is None:
        return

    # print list
    L = root
    while L is not None:
        print(L.data, end=', ')
        L = L.Next
    print('')
    print_level_next_pointer(root.left)


if __name__ == '__main__':
    tree = binary.get_bintree(Node)
    binary.print_level_order(tree)
    con_same_level(tree)
    print('\nprint_level_next_pointer')
    print_level_next_pointer(tree)

    tree = binary.get_bintree(Node)
    print('\ncon_same_level_incomplete')
    con_same_level_incomplete(tree)
    print_level_next_pointer(tree)
