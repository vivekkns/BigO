from bst_utils import get_bst, print_bst


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
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            bst_pred_suc.pre = tmp

        if root.right:
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            bst_pred_suc.suc = tmp

if __name__ == '__main__':
    print_bst()
    root = get_bst()

    bst_pred_suc.pre = None
    bst_pred_suc.suc = None

    bst_pred_suc(root, 11)

    print('pre', str(bst_pred_suc.pre))
    print('succ', str(bst_pred_suc.suc))
