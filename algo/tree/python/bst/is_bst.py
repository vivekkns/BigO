from bst_utils import get_bst, print_bst
from sys import maxint as INF


def is_bst_util(root, min, max):
    if root is None:
        return True

    return min <= root.data <= max and \
        is_bst_util(root.left, min, root.data) and \
        is_bst_util(root.right, root.data, max)


def is_bst(root):
    return is_bst_util(root, -INF, INF)


def is_bst_inorder(root, prev):
    if root is None:
        return True

    if not is_bst_inorder(root.left, prev):
        return False

    if root.data < prev[0]:
        return False

    prev[0] = root.data
    return is_bst_inorder(root.right, prev)


if __name__ == '__main__':
    print_bst()
    bst = get_bst()

    print('is_bst = ', is_bst(bst))
    print('is_bst_inorder = ', is_bst_inorder(bst, [-INF]))

    bst.left.left.data = -7
    print('is_bst = ', is_bst(bst))
    print('is_bst_inorder = ', is_bst_inorder(bst, [-INF]))
