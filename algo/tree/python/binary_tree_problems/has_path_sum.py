from bin_tree_utils import get_bintree, print_tree

#
# Algorithm for checking the existence of path with given sum
#


def is_leaf(root):
    return root.left is None and root.right is None


def has_path_sum(root, rsum):
    if root is None:
        return False

    rsum -= root.data

    # reached leaf and rsum is 0
    if is_leaf(root) and rsum == 0:
        return True
    else:
        return has_path_sum(root.left, rsum) or \
               has_path_sum(root.right, rsum)

if __name__ == '__main__':
    print_tree()
    btree = get_bintree()

    print('has_path_sum(22)? = ', has_path_sum(btree, 22))
    print('has_path_sum(-45)? = ', has_path_sum(btree, -45))
    print('has_path_sum(11)? = ', has_path_sum(btree, 11))
