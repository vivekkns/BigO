class Queue(list):
    def enqueue(self, data):
        self.append(data)

    def dequeue(self):
        return self.pop(0)

    def front(self):
        return self[0]

    def isempty(self):
        return len(self) == 0


class Stack(list):
    def push(self, data):
        self.append(data)

    def isempty(self):
        return len(self) == 0


class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
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


def get_bintree(nodeT=Node):
    root = nodeT(10)
    root.left = nodeT(0)
    root.right = nodeT(-3)

    root.left.left = nodeT(2)
    root.left.right = nodeT(5)
    root.right.left = nodeT(11)
    root.right.right = nodeT(15)

    root.left.left.left = nodeT(-6)
    root.left.right.left = nodeT(-60)

    root.left.left.left.left = nodeT(19)

    return root
