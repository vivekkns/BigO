class PriorityMapQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.A = [None] * self.capacity
        # map stores key -> corresponding item position in the array
        self.map = dict()

    def add(self, item):
        """
        [0] -> Key
        [1] -> Priority
        """

        if self.size == self.capacity:
            raise Exception('Queue overflow')

        i = self.size
        self.A[i] = item
        self.map[item[0]] = i
        self.size += 1
        self._decrease(i)

    def contains(self, key):
        return key in self.map

    def isempty(self):
        return self.size == 0

    def _swap(self, i, j):
        self.map[self.A[i][0]] = j
        self.map[self.A[j][0]] = i
        self.A[i], self.A[j] = self.A[j], self.A[i]

    def _decrease(self, i):
        while self.A[i/2][1] > self.A[i][1]:
            self._swap(i, i/2)
            i = i/2

    def decrease_key(self, key, newpri):
        i = self.map[key]
        self.A[i] = (key, newpri)
        self._decrease(i)

    def extract_min(self):
        if self.size == 0:
            raise Exception('Queue underflow')

        min_item = self.A[0]
        min_key = min_item[0]

        del self.map[min_key]

        self.size -= 1
        self.A[0] = self.A[self.size]
        self._heapify(0)

        return min_item

    def _heapify(self, i):
        c1 = 2*i + 1
        c2 = 2*i + 2

        m = i

        if c1 < self.size and self.A[c1][1] < self.A[m][1]:
            m = c1

        if c2 < self.size and self.A[c2][1] < self.A[m][1]:
            m = c2

        if m != i:
            self._swap(m, i)
            self._heapify(m)