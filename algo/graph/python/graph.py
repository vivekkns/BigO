from collections import defaultdict

#  Graph representation

# 1. Adjacency matrix
# [[0] * |V|] * |V|
#
# 2. Adjacency list
# [ [], [], [], [] ... []]
#

#
#
#
#
#


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addUEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, v, visited=None):
        if visited is None:
            visited = [False] * len(self.graph)
            
        print('visited=', v)
        visited[v] = True
        for e in self.graph[v]:
            if not visited[e]:
                self.DFS(e, visited)

if __name__ == '__main__':
    g = Graph()
    g.addUEdge(0, 1)
    g.addUEdge(1, 7)
    g.addUEdge(1, 2)
    g.addUEdge(2, 4)
    g.addUEdge(2, 3)
    g.addUEdge(4, 5)
    g.addUEdge(4, 6)
    g.addUEdge(4, 7)

    print(g.graph)

    g.DFS(0)

