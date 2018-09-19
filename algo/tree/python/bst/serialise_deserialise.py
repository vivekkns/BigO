from bin_tree_utils import get_bintree, print_tree, Node, Stack
from are_identical_mirror import are_structurally_identical

MARKER = ', '


def get_pre_order_traversal(root, trav_list):
    if root is None:
        return
    trav_list.append(root.data)
    get_pre_order_traversal(root.left, trav_list)
    get_pre_order_traversal(root.right, trav_list)


def construct_bst_pre_order_util(t_list, key, mini, maxi):
    if construct_bst_pre_order_util.index >= len(t_list):
        return None
    root = None
    if mini <= key <= maxi:
        root = Node(key)
        construct_bst_pre_order_util.index += 1
        root.left = construct_bst_pre_order_util(t_list, t_list[construct_bst_pre_order_util.index], mini, key)
        root.right = construct_bst_pre_order_util(t_list, t_list[construct_bst_pre_order_util.index], key, maxi)
    return root


def construct_bst_pre_order(t_list):
    construct_bst_pre_order_util.index = 0
    return construct_bst_pre_order_util(t_list, t_list[0], float('-inf'), float('inf'))


if __name__ == '__main__':
    tree = get_bintree()
    print_tree()
    trav_list = []
    get_pre_order_traversal(tree, trav_list)
    c_tree = construct_bst_pre_order(trav_list)
    print(trav_list)

    trav_list = []
    get_pre_order_traversal(c_tree, trav_list)
    print(trav_list)
    print(are_structurally_identical(tree, c_tree))
