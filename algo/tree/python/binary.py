from __future__ import print_function
import sys
from stack.python.stack import Stack_List as Stack
from queue.python.queue import Queue_list as Queue


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#
#   building tree for experimenting
#


def print_tree():
    btree = """
                10
            /      \\
           0        -3
        /  \       /   \\
       2    5     11   15
     /     /
    -6    -60
    /
   19
"""
    print(btree)


def get_bintree():
    root = Node(10)
    root.left = Node(0)
    root.right = Node(-3)

    root.left.left = Node(2)
    root.left.right = Node(5)
    root.right.left = Node(11)
    root.right.right = Node(15)

    root.left.left.left = Node(-6)
    root.left.right.left = Node(-60)

    root.left.left.left.left = Node(19)

    return root

#
# The following function will return
# the root of copied tree
#
# We can't pass reference in python
# https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
#


def copy_tree(root):
    if root is None:
        return None

    temp = Node(root.data)

    if root.left is not None:
        temp.left = copy_tree(root.left)
    if root.right is not None:
        temp.right = copy_tree(root.right)

    return temp


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


def print_level_order_using_queue(root):
    q = Queue()
    if root is None:
        return
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
    for l in xrange(1, h+1):
        print_level(root, l)


def print_reverse_level_order(root):
    h = height_of_tree(root)
    for l in xrange(h, 0, -1):
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
# check mirror of each there
#


def are_mirrors(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return root1.data == root2.data and \
        are_mirrors(root1.left, root2.right) and \
        are_mirrors(root1.right, root2.left)

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

#
# Given a binary tree, print out all of its root-too-leaf paths
#


def print_paths(root, path=None, pathlen=0):
    if path is None:
        path = []

    if root is None:
        return

    if len(path) > pathlen:
        path[pathlen] = root.data
    else:
        path.insert(pathlen, root.data)

    pathlen += 1

    if root.left is None and root.right is None:
        print([d for d in path[:pathlen]])
    else:
        print_paths(root.left, path, pathlen)
        print_paths(root.right, path, pathlen)

#
# Algorithm for checking the existence of path with given sum
#


def existpathsum(root, rsum):
    if root is None:
        return False

    is_leaf = root.left is None and \
              root.right is None

    rsum -= root.data
    # reached leaf and rsum is
    if is_leaf and rsum == 0:
        return True
    else:
        return existpathsum(root.left, rsum) or \
               existpathsum(root.right, rsum)


#
# The following problem can also be solved using
# Level order traversal using Queue without recursion
#
def sum_all_elements(root):
    if root is None:
        return 0
    else:
        return root.data + \
               sum_all_elements(root.left) + \
               sum_all_elements(root.right)


#
# converting a tree to its mirror
#

def mirror(root):
    if root is None:
        return
    mirror(root.right)
    mirror(root.left)
    temp = root.right
    root.right = root.left
    root.left = temp


#
# Least common ancestor
#


def lca(root, node1, node2):
    if root is None:
        return

    if root is node1 or root is node2:
        return root

    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    # if both left and right are not None means,
    # node1 is present in one subtree node2 in other subtree
    if left is not None and right is not None:
        return root
    elif left is not None:
        return left
    else:
        return right


if __name__ == '__main__':
    print_tree()
    btree = get_bintree()

    print('\n In order = ', end='')
    in_order(btree)

    print('\n Pre order = ', end='')
    pre_order(btree)

    print('\n Post order = ', end='')
    post_order(btree)

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

    print('\n max in tree = ', find_max(btree))

    print('\n is_element_exist(root, 0)= %s' % str(is_element_exist(btree, 0)))
    print('\n is_element_exist(root, -90)= %s' % str(is_element_exist(btree, -90)))

    print(' \n size_of_tree = %d' % size_of_tree(btree))
    print(' \n height_of_tree = %d' % height_of_tree(btree))
    print(' \n num_of_leaves = %d' % num_of_leaves(btree))
    print(' \n num_of_full_nodes = %d' % num_of_full_nodes(btree))
    print(' \n num_half_nodes = %d' % num_half_nodes(btree))

    print(' \n diameter = %d' % diameter(btree))

    print(' \n findlevelwithmaxsum = %s' % str(findlevelwithmaxsum(btree)))

    print('All the paths')
    print_paths(btree)

    print('Existpathsum(22)? = ', existpathsum(btree, 22))
    print('Existpathsum(11)? = ', existpathsum(btree, 11))

    print('sum_all_elements = ', sum_all_elements(btree))

    print('\n\nmirroring tree...')
    print('Before mirror, level order= ')
    print_level_order(btree)
    mirror(btree)
    print('\nAfter mirror, level order= ')
    print_level_order(btree)
    mirror(btree)
    print('\n\ncopying tree..')
    print('Original tree''s level order= ')
    print_level_order(btree)

    n_btree = copy_tree(btree)

    print('\nCopied tree''s level order= ')
    print_level_order(n_btree)

    print('\nare_structurally_identical ?',
          are_structurally_identical(btree, n_btree))

    print('mirroring...')
    mirror(n_btree)
    print('are_structurally_identical ?',
          are_structurally_identical(btree, n_btree))

    print('\nAre mirrors?', are_mirrors(btree, n_btree))

    node1 = btree.left.left.left.left   # 19
    node2 = btree.left.right.left       # -60

    print('lca of node (%d) and (%d) is : (%d)' % (node1.data, node2.data,
          lca(btree, node1, node2).data))

