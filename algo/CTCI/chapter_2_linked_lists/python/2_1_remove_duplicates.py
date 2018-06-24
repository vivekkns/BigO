#
# 2.1 Remove dups: Write code to remove duplicates from an unsorted linked list
#
from __future__ import print_function


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def addTail(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = Node(data)

    def show(self):
        L = []
        n = self.head
        while n is not None:
            L.append(n.data)
            print(n.data, ' -> ', end='')
            n = n.next
        print('None')
        return L

    def remove_dup(self):
        if self.head is None:
            return

        n1 = self.head
        n2 = n1.next

        tbl = dict()
        tbl[n1.data] = 1

        while n2 is not None:
            if n2.data not in tbl:
                n1.next = n2
                n1 = n1.next
                tbl[n1.data] = 1
            n2 = n2.next
        n1.next = None

    def kth_to_last_element(self, k):
        if self.head is None or k <= 0:
            return None

        # Two pointer approach
        p1 = p2 = self.head

        # Move p2 to k positions ahead to p1
        for i in range(k):
            p2 = p2.next
            if p2 is None:
                return None

        # Now move p1 and p2 one step,
        # until p2 reaches last node
        while p2 is not None:
            p2 = p2.next
            p1 = p1.next
        return p1.data


def kth_to_last_element_recur(node, k):
    if node is None:
        return 0
    else:
        i = kth_to_last_element_recur(node.next, k) + 1
        if i == k:
            print(node.data)
        return i

pos = 0


def kth_to_last_element_recur_pos(node, k):
    global pos
    result = node
    if node is not None:
        result = kth_to_last_element_recur_pos(node.next, k)
        pos += 1
        if pos == k:
            result = node

    return result


def kth_to_last_element_recur_no_global(node, k, level=None):
    if level is None:
        # A hack to send a pointer like in C
        level = [0]
    result = node
    if node is not None:
        result = kth_to_last_element_recur_no_global(node.next, k, level)
        level[0] += 1
        if level[0] == k:
            result = node
    return result

if __name__ == '__main__':
    L = LinkedList()
    L.addTail(20)
    L.add(1)
    L.add(4)
    L.add(8)
    L.add(4)
    L.add(11)
    L.add(2)
    L.show()

    L.remove_dup()
    L.show()

    print(L.kth_to_last_element(1))
    print(kth_to_last_element_recur_pos(L.head, 1).data)
    print(kth_to_last_element_recur_no_global(L.head, 1).data)
    kth_to_last_element_recur(L.head, 1)
