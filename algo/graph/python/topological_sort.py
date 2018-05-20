from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        _ = self.graph[v]

    def topological_sort_util(self, v=None, visited=None, stack=None):
        visited[v] = True
        for u in self.graph[v]:
            if not visited[u]:
                self.topological_sort_util(u, visited, stack)

        # At this point there is no edge to unvisited vertex from v
        stack.append(v)

    def topological_sort(self):
        #
        # Only for DAG
        #
        visited = [False] * len(self.graph)
        stack = []
        for v in range(len(self.graph)):
            if not visited[v]:
                self.topological_sort_util(v, visited, stack)
        stack.reverse()
        print(stack)

if __name__ == '__main__':

    print('---- Topological sort ----')
    g = Graph()
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.topological_sort()
