from bin_tree_utils import get_bintree, print_tree


def num_of_leaves(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1
    else:
        return num_of_leaves(root.left) + num_of_leaves(root.right)


#
# A set of all nodes with both left and right children are called full nodes
#

def num_of_full_nodes(root):
    if root is None:
        return 0

    if root.left is not None and root.right is not None:
        return 1 + num_of_full_nodes(root.left) + num_of_full_nodes(root.right)
    elif root.left is not None:
        return num_of_full_nodes(root.left)
    elif root.right is not None:
        return num_of_full_nodes(root.right)
    else:
        return 0


#
# Num of half nodes = nodes with only one children
#

def num_half_nodes(root):

    if root is None:
        return 0

    if root.left and root.right:
        return num_half_nodes(root.left) + num_half_nodes(root.right)
    elif root.left:
        return 1 + num_half_nodes(root.left)
    elif root.right:
        return 1 + num_half_nodes(root.right)
    else:
        return 0


if __name__ == '__main__':
    print_tree()
    btree = get_bintree()

    print(' \n num_of_leaves = %d' % num_of_leaves(btree))
    print(' \n num_of_full_nodes = %d' % num_of_full_nodes(btree))
    print(' \n num_half_nodes = %d' % num_half_nodes(btree))