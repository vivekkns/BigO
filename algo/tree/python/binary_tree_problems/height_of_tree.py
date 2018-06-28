from bin_tree_utils import get_bintree, print_tree


def height_of_tree(root):
    if root is None:
        return 0
    return 1 + max(height_of_tree(root.left), height_of_tree(root.right))


if __name__ == '__main__':
    print_tree()
    btree = get_bintree()
    print(' \n height_of_tree = %d' % height_of_tree(btree))
