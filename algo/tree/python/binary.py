import sys
from stack.python.stack import Stack
from queue.python.queue import Queue_list as Queue


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#
#   building tree for experimenting
#


def get_bintree():
    root = Node(10)
    root.left = Node(0)
    root.right = Node(-3)

    root.left.left = Node(2)
    root.left.right = Node(5)
    root.right.left = Node(11)
    root.right.right = Node(15)

    root.left.left.left = Node(-6)

    return root


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    sys.stdout.write('%d, ' % root.data)
    in_order(root.right)


def pre_order(root):
    if root is None:
        return
    sys.stdout.write('%d, ' % root.data)
    in_order(root.left)
    in_order(root.right)


def post_order(root):
    if root is None:
        return
    in_order(root.left)
    in_order(root.right)
    sys.stdout.write('%d, ' % root.data)


def level_order(root):
    vals = []
    q = Queue()
    if root is None:
        return
    q.enqueue(root)

    while not q.isempty():
        ele = q.dequeue()
        vals.append(ele.data)
        if ele.left:
            q.enqueue(ele.left)
        if ele.right:
            q.enqueue(ele.right)

    return vals

#
# Finding maximum element in the binary tree
#


def find_max(root):
    if root is None:
        return

    l = find_max(root.left)
    r = find_max(root.right)

    m = root.data
    if l is not None and l > m:
        m =l
    if r is not None and r > m:
        m = r
    return m


def is_element_exist(root, data):
    if root is None:
        return False

    if root.data == data:
        return True

    return is_element_exist(root.left, data) or \
        is_element_exist(root.right, data)

if __name__ == '__main__':
    btree = get_bintree()
    print('\nIn order')
    in_order(btree)
    print('\nPre order')
    pre_order(btree)
    print('\nPost order')
    post_order(btree)

    print '\nmax= ', find_max(btree)

    print '\n is_element_exist(root, 0)= %s' % str(is_element_exist(btree, 0))
    print '\n is_element_exist(root, -90)= %s' % str(is_element_exist(btree, -90))

    print ' \n level order = %s' % str(level_order(btree))
