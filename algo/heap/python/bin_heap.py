import random

# Min heap ->
# the key at root must be minimum among all keys present in Binary heap


# represented using array
# A[0] -> root
# A[i/2] -> parent node of i(th) node
# A[2*i + 1] -> left child
# A[2*i + 2] -> right child

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


class MinHeap:
    def __init__(self, capacity):
        self.max_capacity = capacity
        self.A = [0] * capacity
        self.heap_size = 0

    def __str__(self):
        return str(self.A[:self.heap_size])

    def insert_key(self, value):
        if self.heap_size == self.max_capacity:
            raise Exception('Overflow')

        i = self.heap_size
        self.A[i] = value
        self.heap_size += 1

        #
        # Since we are inserting element in the end
        # we only have to check parents
        #
        while i > 0 and self.A[i/2] > self.A[i]:
            swap(self.A, i/2, i)
            i = (i-1)/2

    def extract_min(self):
        if self.heap_size <= 0:
            raise Exception('Underflow')

        root = self.A[0]
        self.A[0] = self.A[self.heap_size-1]
        self.heap_size -= 1
        self._heapify(0)
        return root

    def _heapify(self, i):
        """
        heapify always from top to bottom
        """
        l = 2*i + 1
        r = 2*i + 2
        s = i
        if l < self.heap_size and self.A[l] < self.A[s]:
            s = l
        if r < self.heap_size and self.A[r] < self.A[s]:
            s = r
        if s != i:
            swap(self.A, i, s)
            self._heapify(s)

    def build_heap(self, A):
        self.A = A
        self.max_capacity = len(A)
        self.heap_size = len(A)

        mid = self.heap_size/2
        for i in xrange(mid, -1, -1):
            self._heapify(i)

    def sort(self):
        while self.heap_size > 0:
            swap(self.A, 0, self.heap_size-1)
            self.heap_size -= 1
            self._heapify(0)

    def _reverse(self, left, right):
        if right < left:
            return
        swap(self.A, left, right)
        self._reverse(left+1, right-1)

    def reverse(self):
        self._reverse(0, len(self.A)-1)


def heap_sort_example():
    A = random.sample(xrange(1, 100), 10)
    m = MinHeap(0)
    m.build_heap(A)
    m.sort()
    print A
    m.reverse()
    print A

if __name__ == '__main__':

    heap_sort_example()
    #
    # m = MinHeap(10)
    # m.insert_key(10)
    # m.insert_key(3)
    # m.insert_key(25)
    # m.insert_key(1)
    # m.insert_key(0)
    # m.insert_key(100)
    # m.insert_key(-4)
    #
    # print m
    # while True:
    #     try:
    #         print m.extract_min()
    #     except Exception:
    #         break
    # print m
