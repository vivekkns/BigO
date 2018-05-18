from collections import defaultdict

#  Graph representation

# 1. Adjacency matrix
# [[0] * |V|] * |V|
#
# 2. Adjacency list
# [ [], [], [], [] ... []]
#


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, v, visited=None):
        if visited is None:
            visited = dict()
            for i in self.graph:
                visited[i] = False
        print('visited=', v)
        visited[v] = True
        for e in self.graph[v]:
            if not visited[e]:
                self.DFS(e, visited)

if __name__ == '__main__':
    g = Graph()
    g.addEdge('A', 'B')
    g.addEdge('B', 'H')
    g.addEdge('B', 'C')
    g.addEdge('C', 'E')
    g.addEdge('C', 'D')
    g.addEdge('E', 'F')
    g.addEdge('E', 'G')
    g.addEdge('E', 'H')

    print(g.graph)

    g.DFS('A')

