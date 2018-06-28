from bin_tree_utils import get_bintree, print_tree


def element_exist(root, data):
    if root is None:
        return False

    if root.data == data:
        return True

    return element_exist(root.left, data) or \
        element_exist(root.right, data)

if __name__ == '__main__':
    print_tree()
    btree = get_bintree()
    print('\n is_element_exist(root, 0)= %s' % str(element_exist(btree, 0)))
    print('\n is_element_exist(root, -90)= %s' % str(element_exist(btree, -90)))
