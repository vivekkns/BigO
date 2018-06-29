from bin_tree_utils import Queue
from bin_tree_utils import get_bintree, print_tree

#
# Finding level with maximum sum
#


def find_level_with_maxsum(root):
    if root is None:
        return None

    Q = Queue()
    Q.enqueue(root)
    Q.enqueue(None)

    max_sum = root.data
    max_level = 0

    cur_sum = 0
    level = 0

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
    print_tree()
    btree = get_bintree()
    print('find_level_with_maxsum = %s' % str(find_level_with_maxsum(btree)))
