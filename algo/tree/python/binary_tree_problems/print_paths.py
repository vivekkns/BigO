from bin_tree_utils import get_bintree, print_tree


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

if __name__ == '__main__':
    print_tree()
    btree = get_bintree()

    print('All the paths')
    print_paths(btree)
