from __future__ import print_function
from bin_tree_utils import Queue, get_bintree, print_tree
from traversals import print_level_order

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


def con_same_level_bfs(root):
    q = Queue()
    q.enqueue(root)
    q.enqueue(None)

    t2 = None
    while not q.isempty():
        t1 = q.dequeue()

        if t1 is None:
            if not q.isempty():
                q.enqueue(None)
        else:
            if t1.left is not None:
                q.enqueue(t1.left)
            if t1.right is not None:
                q.enqueue(t1.right)

        if t2 is not None:
            t2.Next = t1
        t2 = t1


# Single while loop
def con_same_level_bfs_1(root):
    q = Queue()
    q.enqueue(root)
    q.enqueue(None)

    while not q.isempty():
        t1 = q.dequeue()

        if t1 is None:
            if not q.isempty():
                q.enqueue(None)
        else:
            if t1.left is not None:
                q.enqueue(t1.left)
            if t1.right is not None:
                q.enqueue(t1.right)
            t1.Next = q.front()


def get_first_node(node):
    # keep traversing the list till we
    # find a valid node
    while node is not None:
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
    print_tree()

    tree = get_bintree(Node)
    print('\ncon_same_level_incomplete')
    con_same_level_incomplete(tree)
    print_level_next_pointer(tree)

    tree = get_bintree(Node)
    print('\ncon_same_level_bfs')
    con_same_level_bfs(tree)
    print_level_next_pointer(tree)

    tree = get_bintree(Node)
    print('\ncon_same_level_bfs_1')
    con_same_level_bfs_1(tree)
    print_level_next_pointer(tree)
