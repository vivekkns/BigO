from __future__ import print_function
from maxheap import MaxHeap

# Tuples and lists are compared lexicographically using comparison of corresponding elements.
# This means that to compare equal, each element must compare equal and
# the two sequences must be of the same type and have the same length.


def dist2(p):
    return p[0]*p[0] + p[1]*p[1]


def get_dist(P):
    d = []
    for p in P:
        d.append((dist2(p), p))
    return d


def k_closest(P, k):
    n = len(P)
    d = get_dist(P)

    h = MaxHeap()
    h.build(d, k)

    for i in range(k, n):
        if h.get_max() > d[i]:
            h.decrease_max(d[i])

    return [p[1] for p in h.A[:k]]


def k_closest_space_efficient(P, k):
    n = len(P)

    # build maxheap only for first k elements, S:O(k)
    d = []
    for i in range(k):
        d.append((dist2(P[i]), P[i]))

    h = MaxHeap()
    h.build(d, k)
    for i in range(k, n):
        dp = (dist2(P[i]), P[i])
        if h.get_max() > dp:
            h.decrease_max(dp)

    return [p[1] for p in h]

if __name__ == '__main__':
    P = [(1, 1), (-4, 7), (0, 2), (12, 15), (-1, -2), (-1, -3), (10, 2), (6, 7)]
    print (k_closest(P, 4))
    print (k_closest_space_efficient(P, 4))
