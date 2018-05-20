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
        _ = self.graph[v]

    def DFS_util(self, v, visited):
        print('visited=', v)
        visited[v] = True
        for u in self.graph[v]:
            if not visited[u]:
                self.DFS_util(u, visited)

    def DFS(self, v):
        visited = [False] * len(self.graph)
        self.DFS_util(v, visited)

    def BFS(self, v):
        visited = [False] * len(self.graph)
        q = list()
        q.append(v)
        while len(q) > 0:
            t = q.pop()
            if not visited[t]:
                print('visited=', t)
                visited[t] = True
            for u in self.graph[t]:
                if not visited[u]:
                    q.append(u)

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

    print('----- DFS -----')
    g.DFS(0)

    print('----- BFS -----')
    g.BFS(0)
