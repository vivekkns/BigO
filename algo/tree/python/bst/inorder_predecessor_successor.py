from bst_utils import get_bst, print_bst


def find_max(root):
    while root.right:
        root = root.right
    return root


def find_min(root):
    while root.left:
        root = root.left
    return root


def bst_pred_suc(root, data):
    if not root:
        return None

    if data < root.data:
        bst_pred_suc.suc = root
        bst_pred_suc(root.left, data)
    elif data > root.data:
        bst_pred_suc.pre = root
        bst_pred_suc(root.right, data)
    else:
        if root.left:
            bst_pred_suc.pre = find_max(root.left)

        if root.right:
            bst_pred_suc.suc = find_min(root.right)

if __name__ == '__main__':
    print_bst()
    root = get_bst()

    bst_pred_suc.pre = None
    bst_pred_suc.suc = None

    bst_pred_suc(root, 11)

    print('pre', str(bst_pred_suc.pre))
    print('succ', str(bst_pred_suc.suc))
