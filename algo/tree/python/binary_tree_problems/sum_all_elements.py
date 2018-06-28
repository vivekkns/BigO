from bin_tree_utils import get_bintree, print_tree

#
# The following problem can also be solved using
# Level order traversal using Queue without recursion
#


def sum_all_elements(root):
    if root is None:
        return 0
    else:
        return root.data + \
               sum_all_elements(root.left) + \
               sum_all_elements(root.right)


if __name__ == '__main__':
    print_tree()
    btree = get_bintree()

    print('sum_all_elements = ', sum_all_elements(btree))