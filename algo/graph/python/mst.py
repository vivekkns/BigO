from collections import defaultdict
from heap.python.pqueue import PriorityMapQueue
import sys

INF = sys.maxint


class Node:
    def __init__(self, data):
        self.rank = 0
        self.parent = self
        self.data = data


class DisjointSet:
    def __init__(self):
        self.ds = dict()

    def makeset(self, data):
        n = Node(data)
        # n.parent = n
        # n.rank = 0
        self.ds[data] = n

    def union(self, data1, data2):
        n1 = self.ds[data1]
        n2 = self.ds[data2]

        p1 = self.findset(n1)
        p2 = self.findset(n2)

        if p1 == p2:
            return

        if p1.rank == p2.rank:
            p1.rank += 1
            p2.parent = p1
        elif p1.rank > p2.rank:
            p2.parent = p1
        else:
            p1.parent = p2

    def findset(self, node):
        if node.parent != node:
            node.parent = self.findset(node.parent)
        return node.parent

    def findset_data(self, data):
        return self.findset(self.ds[data]).data


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

    def kruskal(self):
        allEdges = []
        for v in self.adj:
            for u, u_w in self.adj[v]:
                allEdges.append((v, u, u_w))
        allEdges.sort(key=lambda e: e[2])

        num_V = len(self.adj)
        ds = DisjointSet()
        for v in range(num_V):
            ds.makeset(v)

        for u, v, e in allEdges:
            if ds.findset_data(u) != ds.findset_data(v):
                ds.union(u, v)
                print(u, '->', v)

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

    print('Disjoint set example')

    ds = DisjointSet()
    ds.makeset(1)
    ds.makeset(2)
    ds.makeset(3)

    ds.union(1, 2)
    print(ds.findset_data(1))
    print(ds.findset_data(3))
    ds.union(2, 3)
    print(ds.findset_data(1))
    print(ds.findset_data(3))

    print('Kruskal MST')
    g.kruskal()
