from bst_utils import get_bst, print_bst


def find(root, data):
    if root is None:
        return None

    if data < root.data:
        return find(root.left, data)
    elif data > root.data:
        return find(root.right, data)
    else:
        return root


def find_iterative(root, data):
    if root is None:
        return None

    while root is not None:
        if data < root.data:
            root = root.left
        elif data > root.data:
            root = root.right
        else:
            return root
    return None


def find_max(root):
    if root is None:
        return None

    if root.right is None:
        return root
    else:
        return find_max(root.right)


def find_max_recu(root):
    if root is None:
        return None

    while root.right is not None:
        root = root.right
    return root


def find_min(root):
    if root is None:
        return None

    if root.left is None:
        return root
    else:
        return find_min(root.left)


def find_min_recur(root):
    if root is None:
        return None

    while root.left is not None:
        root = root.left

    return root

if __name__ == '__main__':
    print_bst()
    root = get_bst()

    print('find', str(find(root, -6)))
    print('find_iterative', str(find_iterative(root, 8)))
    
    print('find_max', str(find_max(root)))
    print('find_max_recu', str(find_max_recu(root)))

    print('find_min', str(find_min(root)))
    print('find_min_recur', str(find_min_recur(root)))
