
def path_of_node(root, node, path=None, pathlen=0):
    if root is None:
        return
    if path is None:
        path = []

    if len(path) > pathlen:
        path[pathlen] = root
    else:
        path.insert(pathlen, root)

    pathlen += 1
    if root is node:
        return path[:pathlen]

    lp = path_of_node(root.left, node, path, pathlen)
    if lp is not None:
        return lp

    rp = path_of_node(root.right, node, path, pathlen)
    if rp is not None:
        return rp
