from __future__ import print_function


class Node:
    def __init__(self, data):
        self.Prev = None
        self.data = data
        self.Next = None


class LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.Next = self.head
            self.head.Prev = node
            self.head = node
            self.head.Prev = None

    def move_to_front(self, node):
        if node is self.head:
            return

        node.Prev.Next = node.Next
        if node.Next:
            node.Next.Prev = node.Prev
        else:
            # tail node is being moved to front
            self.tail = node.Prev

        node.Prev = None
        node.Next = None
        self.insert_front(node)

    def delete_from_end(self):
        if self.tail is self.head:
            del self.tail
            self.head = self.tail = None
            return

        d_node = self.tail
        self.tail = self.tail.Prev
        self.tail.Next = None
        del d_node

    def print_list(self):

        temp = self.head
        while temp:
            print(temp.data, end=', ')
            temp = temp.Next

        print('')


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = dict()
        self.ll = LL()

    # @return an integer
    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.ll.move_to_front(node)
            return node.data[1]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.data = (key, value)
            self.ll.move_to_front(node)
        else:
            if len(self.map) == self.capacity:
                d_key, _ = self.ll.tail.data
                self.ll.delete_from_end()
                del self.map[d_key]

            node = Node((key, value))
            self.map[key] = node
            self.ll.insert_front(node)

        self.ll.print_list()


if __name__ == '__main__':

    c = LRUCache(2)
    c.set(2, 1)
    c.set(1, 1)
    c.set(2, 3)
    c.set(4, 1)

    print(c.get(1))
    print(c.get(2))
