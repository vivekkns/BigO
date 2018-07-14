from bst_utils import get_bst, print_bst
from find_min_max import find_max
from tree.python.binary_tree_problems import traversals


def bst_delete(root, data):
    if not root:
        return None

    if data < root.data:
        root.left = bst_delete(root.left, data)
    elif data > root.data:
        root.right = bst_delete(root.right, data)
    else:
        if root.left and root.right:
            temp = find_max(root.left)
            root.data = temp.data
            root.left = bst_delete(root.left, temp.data)
        elif root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            root = None
    return root


if __name__ == '__main__':
    print_bst()
    bst = get_bst()
    traversals.print_in_order(bst)
    print('\ndeleting node 10')
    bst = bst_delete(bst, 10)
    traversals.print_in_order(bst)

    print('\ndeleting node 8')
    bst = bst_delete(bst, 8)
    traversals.print_in_order(bst)
