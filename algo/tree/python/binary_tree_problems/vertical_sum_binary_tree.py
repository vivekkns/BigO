from __future__ import print_function
from bin_tree_utils import get_bintree, print_tree

hashtbl = dict()


def vertical_sum(root, col):
    if root is None:
        return

    if col in hashtbl:
        hashtbl[col] += root.data
    else:
        hashtbl[col] = root.data

    vertical_sum(root.left, col-1)
    vertical_sum(root.right, col+1)


if __name__ == '__main__':
    print_tree()
    btree = get_bintree()
    vertical_sum(btree, 0)

    print('Vertical sum')
    for k in sorted(hashtbl.keys()):
        print(k, "=>", hashtbl[k])
