from bin_tree_utils import get_bintree, print_tree


def size_of_tree(root):
    if root is None:
        return 0
    else:
        return size_of_tree(root.left) + 1 + size_of_tree(root.right)

if __name__ == '__main__':
    print_tree()
    btree = get_bintree()
    print(' \n size_of_tree = %d' % size_of_tree(btree))
