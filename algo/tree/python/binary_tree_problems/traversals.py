from __future__ import print_function
import bin_tree_utils as utils
from bin_tree_utils import Queue, Stack
from height_of_tree import height_of_tree


def print_in_order(root):
    if root is None:
        return
    print_in_order(root.left)
    print('%d, ' % root.data, end='')
    print_in_order(root.right)


def print_pre_order(root):
    if root is None:
        return
    print('%d, ' % root.data, end='')
    print_pre_order(root.left)
    print_pre_order(root.right)


def print_post_order(root):
    if root is None:
        return
    print_post_order(root.left)
    print_post_order(root.right)
    print ('%d, ' % root.data, end='')


def print_level_order_using_queue(root):
    if root is None:
        return

    q = Queue()
    q.enqueue(root)

    while not q.isempty():
        ele = q.dequeue()
        print(ele.data, end=', ')
        if ele.left:
            q.enqueue(ele.left)
        if ele.right:
            q.enqueue(ele.right)


def print_level_order_using_stack(root):
    #
    # Queue can be realised using two stacks
    #
    if root is None:
        return

    S1 = Stack()
    S2 = Stack()
    S1.push(root)

    while not S1.isempty() or not S2.isempty():
        if S2.isempty():
            while not S1.isempty():
                S2.push(S1.pop())
        ele = S2.pop()
        print(ele.data, end=', ')
        if ele.left:
            S1.push(ele.left)
        if ele.right:
            S1.push(ele.right)


def print_level_order(root):
    h = height_of_tree(root)
    for l in range(1, h+1):
        print_level(root, l)


def print_reverse_level_order(root):
    h = height_of_tree(root)
    for l in range(h, 0, -1):
        print_level(root, l)


def print_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=', ')
    elif level > 1:
        print_level(root.left, level-1)
        print_level(root.right, level-1)


def print_reverse_level_order_stack_queue(root):
    #
    # here python's list (L) is used for Queue and Stack
    # len(L) -> can be used to check the emptiness check
    # stack's push or Queue's enqueue is done L.append()
    # stack's pop -> L.pop()
    # Queue's dequeue -> L.pop(0)

    if root is None:
        return

    S = list()
    Q = list()

    Q.append(root)

    while len(Q):
        root = Q.pop(0)
        S.append(root)

        #
        # Note that, we first push right node
        # before pushing left node into the stack
        #
        if root.right:
            Q.append(root.right)

        if root.left:
            Q.append(root.left)

    while len(S):
        print(S.pop().data, end=', ')


def print_reverse_level_order_stack_recursion(root):
    if root is None:
        return

    Q = list()

    Q.append(root)
    level_order_recursion(Q)


def level_order_recursion(Q):
    while len(Q):
        root = Q.pop(0)
        if root.right:
            Q.append(root.right)

        if root.left:
            Q.append(root.left)

        level_order_recursion(Q)
        print(root.data, end=', ')


if __name__ == '__main__':
    utils.print_tree()
    btree = utils.get_bintree()

    print('\n In order = ', end='')
    print_in_order(btree)

    print('\n Pre order = ', end='')
    print_pre_order(btree)

    print('\n Post order = ', end='')
    print_post_order(btree)

    print('\n Print Level order = ', end='')
    print_level_order(btree)

    print('\n print_level_order_using_queue = ', end='')
    print_level_order_using_queue(btree)

    print('\n print_level_order_using_stack = ', end='')
    print_level_order_using_stack(btree)

    print('\n Print reverse Level order = ', end='')
    print_reverse_level_order(btree)

    print('\n print_reverse_level_order_stack_queue = ', end='')
    print_reverse_level_order_stack_queue(btree)

    print('\n print_reverse_level_order_stack_recursion = ', end='')
    print_reverse_level_order_stack_recursion(btree)
