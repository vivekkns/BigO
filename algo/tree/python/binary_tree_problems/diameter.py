from bin_tree_utils import get_bintree, print_tree
from height_of_tree import height_of_tree


def diameter(root):
    if root is None:
        return 0
    hl = height_of_tree(root.left)
    hr = height_of_tree(root.right)

    dl = diameter(root.left)
    dr = diameter(root.right)
    return max(dl, dr, hl+hr+1)

if __name__ == '__main__':
    print_tree()
    btree = get_bintree()
    print(' \n diameter = %d' % diameter(btree))