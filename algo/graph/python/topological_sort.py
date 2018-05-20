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

    def topological_sort_queue(self):

        num_v = len(self.graph)

        # calc indegree
        indegree = [0] * num_v
        for v in self.graph:
            for e in self.graph[v]:
                indegree[e] += 1

        # add all indegree 0 vertices into the queue
        counter = 0
        topo_sort = [0] * num_v
        q = []
        for v in self.graph:
            if indegree[v] == 0:
                q.append(v)

        while len(q) > 0:
            v = q.pop(0)
            topo_sort[v] = counter
            counter += 1

            for u in self.graph[v]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    q.append(u)
        print([topo_sort.index(k) for k in range(num_v)])

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

    g.topological_sort_queue()
