
#
# Implementation of chaining collision resolution technique
#


class ListNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.Next = None


class HashTable:
    LOAD_FACTOR = 20

    def __init__(self, size):
        self.size = size
        self.tsize = size / self.LOAD_FACTOR

        # Number of elements in the table
        self.count = 0
        self.table = [None] * self.tsize

    def hash(self, key):
        return key % self.tsize

    def search(self, data):
        i = self.hash(data)
        temp = self.table[i]

        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.Next

        return False

    def insert(self, data):
        if self.search(data):
            return False

        i = self.hash(data)

        n = ListNode(i, data)

        if self.table[i] is None:
            self.table[i] = n
        else:
            n.Next = self.table[i]
            self.table[i] = n

        self.count += 1

        if self.count/self.tsize > self.LOAD_FACTOR:
            self.rehash()

        return True

    def delete(self, data):
        i = self.hash(data)
        n = self.table[i]
        if n is None:
            return False

        if n.data == data:
            self.table[i] = n.Next
            del n
        else:
            prev = n
            n = n.Next
            while n is not None:
                if n.data == data:
                    prev.Next = n.Next
                    del n
                    break
                prev = n
                n = n.Next
        return True

    def rehash(self):
        old_table = self.table

        self.tsize *= 2
        self.table = [None] * self.tsize

        for n in old_table:
            while n is not None:
                i = self.hash(n.data)

                if self.table[i] is None:
                    self.table[i] = n
                else:
                    n.Next = self.table[i]
                    self.table[i] = n