from bin_tree_utils import get_bintree, print_tree
from path_of_node import path_of_node

#
# Least common ancestor
#


def lca(root, node1, node2):
    if root is None:
        return

    if root is node1 or root is node2:
        return root

    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    # if both left and right are not None means,
    # node1 is present in one subtree node2 in other subtree
    if left is not None and right is not None:
        return root
    elif left is not None:
        return left
    else:
        return right


def first_diff_element(L1, L2):

    k1 = k2 = 0
    while L1[k1] == L2[k2]:
        k1 += 1
        k2 += 1

    return L1[k1-1]


if __name__ == '__main__':
    print_tree()
    btree = get_bintree()

    node1 = btree.left.left.left.left   # 19
    node2 = btree.left.right.left       # -60

    print('------------------------------')
    print('            LCA              ')
    print('------------------------------')
    print('lca of node (%d) and (%d) is : (%d)' % (node1.data, node2.data,
                                                   lca(btree, node1, node2).data))

    p_node1 = path_of_node(btree, node1)
    print('path of Node(%d) is %s' % (node1.data,
                                      str([k.data for k in p_node1])))

    p_node2 = path_of_node(btree, node2)
    print('path of Node(%d) is %s' % (node2.data,
                                      str([k.data for k in p_node2])))

    print('lca is:', first_diff_element(p_node1, p_node2).data)