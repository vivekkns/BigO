from __future__ import print_function
from bin_tree_utils import get_bintree, print_tree


def print_all_ancestors(root, node):
    if root is None:
        return False

    if root.left is node or \
            root.right is node or \
            print_all_ancestors(root.left, node) or \
            print_all_ancestors(root.right, node):

        print(root.data, end=', ')
        return True

if __name__ == '__main__':
    print_tree()
    btree = get_bintree()
    node = btree.left.left.left

    print('Ancestors to node = ', node.data, ' ... ')
    print_all_ancestors(btree, node)
