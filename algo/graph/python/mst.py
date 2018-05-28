from collections import defaultdict
from heap.python.pqueue import PriorityMapQueue
import sys

INF = sys.maxint


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def adduEdge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def prim(self):
        num_V = len(self.adj)
        q = PriorityMapQueue(num_V)
        dist = [INF] * num_V
        dist[0] = 0
        parent = [None] * num_V

        for v in range(num_V):
            q.add((v, dist[v]))

        while not q.isempty():
            v = q.extract_min()[0]
            print(parent[v], '->', v)
            for u, u_w in self.adj[v]:
                if not q.contains(u):
                    continue
                if dist[u] > u_w:
                    dist[u] = u_w
                    parent[u] = v
                    q.decrease_key(u, u_w)

        print(parent)

if __name__ == '__main__':
    #
    #

    g = Graph()
    g.adduEdge(0, 1, 3)
    g.adduEdge(0, 3, 1)
    g.adduEdge(1, 2, 1)
    g.adduEdge(1, 3, 3)
    g.adduEdge(2, 3, 1)
    g.adduEdge(2, 4, 5)
    g.adduEdge(2, 5, 4)
    g.adduEdge(3, 4, 6)
    g.adduEdge(4, 5, 2)

    g.prim()

