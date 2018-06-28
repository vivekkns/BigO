from bin_tree_utils import get_bintree, print_tree


def find_max(root):
    if root is None:
        return

    l = find_max(root.left)
    r = find_max(root.right)

    m = root.data
    if l is not None and l > m:
        m = l
    if r is not None and r > m:
        m = r
    return m

if __name__ == '__main__':
    print_tree()
    btree = get_bintree()
    print('\n max in tree = ', find_max(btree))