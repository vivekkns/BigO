class MaxHeap:
    def __init__(self, msize=0):
        self.msize = msize
        self.A = [0] * msize
        # size index starts from 1 NOT 0
        self.size = 0

    def _swap(self, i, j):
        self.A[i], self.A[j] = self.A[j], self.A[i]

    def build(self, A, size):
        self.A = A
        self.size = size
        for i in range(self.size/2, -1, -1):
            self.sink(i)

    def swim(self, i):
        while i > 0 and self.A[i] > self.A[(i-1)/2]:
            self._swap(i, (i-1)/2)
            i = (i-1)/2

    def sink(self, i):
        m = i

        l = 2*i + 1
        r = 2*i + 2

        if l < self.size and self.A[l] > self.A[m]:
            m = l
        if r < self.size and self.A[r] > self.A[m]:
            m = r

        if m != i:
            self._swap(i, m)
            self.sink(m)

    def get_max(self):
        return self.A[0]

    def decrease_max(self, data):
        self.A[0] = data
        self.sink(0)

    def __iter__(self):
        for a in self.A:
            yield a
