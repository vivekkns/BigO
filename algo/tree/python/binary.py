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

def print_tree(root):
    pass


def get_bintree():
    root = Node(10)
    root.left = Node(0)
    root.right = Node(-3)

    root.left.left = Node(2)
    root.left.right = Node(5)
    root.right.left = Node(11)
    root.right.right = Node(15)

    root.left.left.left = Node(-6)
    root.left.left.right = Node(-60)

    root.left.left.left.left = Node(19)

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
        m = l
    if r is not None and r > m:
        m = r
    return m


def size_of_tree(root):
    if root is None:
        return 0
    else:
        return size_of_tree(root.left) + 1 + size_of_tree(root.right)


def is_element_exist(root, data):
    if root is None:
        return False

    if root.data == data:
        return True

    return is_element_exist(root.left, data) or \
        is_element_exist(root.right, data)


def height_of_tree(root):
    if root is None:
        return 0
    return 1 + max(height_of_tree(root.left), height_of_tree(root.right))


def num_of_leaves(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1
    else:
        return num_of_leaves(root.left) + num_of_leaves(root.right)


#
# A set of all nodes with both left and right children are called full nodes
#

def num_of_full_nodes(root):
    if root is None:
        return 0

    if root.left is not None and root.right is not None:
        return 1 + num_of_full_nodes(root.left) + num_of_full_nodes(root.right)
    elif root.left is not None:
        return num_of_full_nodes(root.left)
    elif root.right is not None:
        return num_of_full_nodes(root.right)
    else:
        return 0


#
# Num of half nodes = nodes with only one children
#

def num_half_nodes(root):

    if root is None:
        return 0

    if root.left and root.right:
        return num_half_nodes(root.left) + num_half_nodes(root.right)
    elif root.left:
        return 1 + num_half_nodes(root.left)
    elif root.right:
        return 1 + num_half_nodes(root.right)
    else:
        return 0


def are_structurally_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    else:
        return root1.data == root2.data and \
               are_structurally_identical(root1.left, root2.left) and \
               are_structurally_identical(root1.right, root2.right)

#
#   https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
#


def diameter(root):
    if root is None:
        return 0
    hl = height_of_tree(root.left)
    hr = height_of_tree(root.right)

    dl = diameter(root.left)
    dr = diameter(root.right)
    return max(dl, dr, hl+hr+1)


#
# Finding level with maximum sum
#

def findlevelwithmaxsum(root):
    if root is None:
        return None

    max_sum = -100000
    cur_sum = 0

    level = 0
    max_level = 0

    Q = Queue()
    Q.enqueue(root)
    Q.enqueue(None)

    while not Q.isempty():
        temp = Q.dequeue()
        if temp is None:
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_level = level
            cur_sum = 0
            if not Q.isempty():
                Q.enqueue(None)

            level += 1
        else:
            cur_sum += temp.data
            if temp.left:
                Q.enqueue(temp.left)
            if temp.right:
                Q.enqueue(temp.right)

    return max_level, max_sum

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

    print ' \n size_of_tree = %d' % size_of_tree(btree)
    print ' \n height_of_tree = %d' % height_of_tree(btree)
    print ' \n num_of_leaves = %d' % num_of_leaves(btree)
    print ' \n num_of_full_nodes = %d' % num_of_full_nodes(btree)
    print ' \n num_half_nodes = %d' % num_half_nodes(btree)

    print ' \n diameter = %d' % diameter(btree)

    print ' \n findlevelwithmaxsum = %s' % str(findlevelwithmaxsum(btree))

