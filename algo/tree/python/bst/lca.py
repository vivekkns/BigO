from bst_utils import get_bst, print_bst

#
# Least common ancestor
#


def lca(root, node1, node2):

    if node1.data <= root.data <= node2.data or \
            node2.data <= root.data <= node1.data:
        return root

    if node1.data < root.data:
        return lca(root.left, node1, node2)
    else:
        return lca(root.right, node1, node2)

if __name__ == '__main__':
    print_bst()
    bst = get_bst()

    node1 = bst.left.left.left   # -6
    node2 = bst.left.right.left       # 8

    print('------------------------------')
    print('            LCA              ')
    print('------------------------------')
    print('lca of node (%d) and (%d) is : (%d)' % (node1.data, node2.data,
                                                   lca(bst, node1, node2).data))
