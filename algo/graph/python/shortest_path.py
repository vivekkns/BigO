from collections import defaultdict
from pprint import pprint as pp
import sys
INF = sys.maxint


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


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def addedge(self, u, v, w=None):
        if w is None:
            self.adj[u].append(v)
        else:
            self.adj[u].append((v, w))
        _ = self.adj[v]

    def ssp_unweighted(self, s):
        num_v = len(self.adj)
        dist = [None] * num_v
        parent = [None] * num_v
        dist[s] = 0
        q = [s]

        while len(q) > 0:
            v = q.pop(0)
            for u in self.adj[v]:
                if dist[u] is None:
                    dist[u] = dist[v] + 1
                    parent[u] = v
                    q.append(u)
        return dist, parent

    def dijkstra(self, s):
        num_v = len(self.adj)
        dist = [INF] * num_v
        parent = [None] * num_v
        dist[s] = 0

        q = PriorityMapQueue(num_v)
        for v in range(num_v):
            q.add((v, dist[v]))

        while not q.isempty():
            v = q.extract_min()[0]
            for u, u_w in self.adj[v]:
                if not q.contains(u):
                    continue
                new_d = dist[v] + u_w
                if dist[u] > new_d:
                    dist[u] = new_d
                    parent[u] = v
                    q.decrease_key(u, new_d)

        return dist, parent

    def bellman_ford(self, s):
        num_v = len(self.adj)

        parent = [None] * num_v
        dist = [INF] * num_v
        dist[s] = 0

        # Relax all edges (|V| - 1) times
        for _ in range(num_v - 1):
            for v in range(num_v):
                for u, u_w in self.adj[v]:
                    new_d = dist[v] + u_w
                    if new_d < dist[u]:
                        dist[u] = new_d
                        parent[u] = v

        # detecting -ve cycle in the graph
        is_valid = True
        for v in self.adj:
            for u, u_w in self.adj[v]:
                if dist[u] > dist[v] + u_w:
                    is_valid = False
                    break
            if not is_valid:
                break

        return dist, parent, is_valid

if __name__ == '__main__':
    g = Graph()
    g.addedge(0, 1)
    g.addedge(0, 3)
    g.addedge(1, 3)
    g.addedge(1, 4)
    g.addedge(2, 0)
    g.addedge(2, 5)
    g.addedge(3, 5)
    g.addedge(3, 6)
    g.addedge(4, 6)
    g.addedge(6, 5)

    pp(g.ssp_unweighted(0))

    g = Graph()
    g.addedge(0, 1, 4)
    g.addedge(0, 2, 1)
    g.addedge(1, 4, 4)
    g.addedge(2, 1, 2)
    g.addedge(2, 3, 4)
    g.addedge(3, 4, 4)

    pp(g.dijkstra(0))
    pp(g.bellman_ford(0))