from bin_tree_utils import Node, get_bintree, print_tree
from traversals import print_level_order

#
# The following function will return
# the root of copied tree
#
# We can't pass reference in python
# https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
#


def copy_tree(root):
    if root is None:
        return None

    temp = Node(root.data)

    if root.left is not None:
        temp.left = copy_tree(root.left)
    if root.right is not None:
        temp.right = copy_tree(root.right)

    return temp


if __name__ == '__main__':
    print_tree()
    btree = get_bintree()

    print('\n\ncopying tree..')
    print('Original tree''s level order= ')
    print_level_order(btree)

    n_btree = copy_tree(btree)

    print('\nCopied tree''s level order= ')
    print_level_order(n_btree)


