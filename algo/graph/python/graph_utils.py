#  Graph representation

# 1. Adjacency matrix
# [[0] * |V|] * |V|
#
# 2. Adjacency list
# [ [], [], [], [] ... []]
#


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


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = dict()
        for v in range(V):
            self.adj[v] = list()

    def addUEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def addEdge(self, u, v):
        self.adj[u].append(v)
