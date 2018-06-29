from __future__ import print_function
from bin_tree_utils import get_bintree, print_tree, Stack


def print_zig_zag(root):

    c_s = Stack()
    n_s = Stack()

    l2r = True

    c_s.push(root)

    while not c_s.isempty():
        t = c_s.pop()
        print(t.data, end=', ')
        if l2r:
            if t.left is not None:
                n_s.push(t.left)
            if t.right is not None:
                n_s.push(t.right)
        else:
            if t.right is not None:
                n_s.push(t.right)
            if t.left is not None:
                n_s.push(t.left)

        if c_s.isempty():
            n_s, c_s = c_s, n_s
            l2r = not l2r

if __name__ == '__main__':
    print_tree()
    btree = get_bintree()
    print_zig_zag(btree)
