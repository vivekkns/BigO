from __future__ import print_function

from bin_tree_utils import Node
from traversals import print_in_order, print_pre_order

#
# Building tree from traversal
#
# Tree can be uniquely reconstructed using
#       in-order + {pre, post, level}
#
# Without in-order even if all pre, post, level traversal are given,
# it is not possible to reconstructed
#


def build_tree(in_order, pre_order, preindex, in_start, in_end):
    if in_end < in_start:
        return
    data = pre_order[preindex[0]]
    preindex[0] += 1
    root = Node(data)
    i = in_order.index(data)
    root.left = build_tree(in_order, pre_order, preindex, in_start, i-1)
    root.right = build_tree(in_order, pre_order, preindex, i+1, in_end)
    return root

if __name__ == '__main__':

    in_order = [19, -6, 2, 0, -60, 5, 10, 11, -3, 15]
    pre_order = [10, 0, 2, -6, 19, 5, -60, -3, 11, 15]

    print('in_order = ', in_order)
    print('pre_order = ', pre_order)

    bu_tree = build_tree(in_order, pre_order, [0], 0, len(in_order)-1)

    print()

    print('In order = ', end='')
    print_in_order(bu_tree)

    print()

    print('Pre order = ', end='')
    print_pre_order(bu_tree)
