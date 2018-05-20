from collections import defaultdict
from pprint import pprint as pp


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self, u, v, w=None):
        if w is None:
            self.graph[u].append(v)
        else:
            self.graph[u].append({'v': v, 'w': w})
        _ = self.graph[v]

    def ssp_unweighted(self, s):
        num_v = len(self.graph)
        # first column is for storing distance
        # second column is for storing pre
        tbl = {v: {'dist': None, 'path': None} for v in range(num_v)}
        tbl[s]['dist'] = 0
        q = [s]
        while len(q) > 0:
            v = q.pop(0)
            for u in self.graph[v]:
                if tbl[u]['dist'] is None:
                    tbl[u]['dist'] = tbl[v]['dist'] + 1
                    tbl[u]['path'] = v
                    q.append(u)

        return tbl

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
