from bin_tree_utils import get_bintree, print_tree
from copy_tree import copy_tree
from mirror_tree import mirror_tree


def are_structurally_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    else:
        return root1.data == root2.data and \
               are_structurally_identical(root1.left, root2.left) and \
               are_structurally_identical(root1.right, root2.right)

#
# check mirror of each there
#


def are_mirrors(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return root1.data == root2.data and \
        are_mirrors(root1.left, root2.right) and \
        are_mirrors(root1.right, root2.left)


if __name__ == '__main__':
    print_tree()
    btree = get_bintree()
    n_btree = copy_tree(btree)

    print('\nare_structurally_identical ?',
          are_structurally_identical(btree, n_btree))

    print('mirroring...')
    mirror_tree(n_btree)
    print('are_structurally_identical ?',
          are_structurally_identical(btree, n_btree))

    print('\nAre mirrors?', are_mirrors(btree, n_btree))
