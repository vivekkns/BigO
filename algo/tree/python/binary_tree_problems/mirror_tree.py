from bin_tree_utils import get_bintree, print_tree
from traversals import print_level_order


def mirror_tree(root):
    if root is None:
        return
    temp = root.right
    root.right = root.left
    root.left = temp
    mirror_tree(root.right)
    mirror_tree(root.left)


if __name__ == '__main__':
    print_tree()
    btree = get_bintree()

    print('\n\nmirroring tree...')

    print('Before mirror, level order= ')
    print_level_order(btree)

    mirror_tree(btree)

    print('\nAfter mirror, level order= ')
    print_level_order(btree)

    mirror_tree(btree)

    print('\nAfter mirror, level order= ')
    print_level_order(btree)