from __future__ import print_function


def append_skyline(result, sk):
    if not len(result):
        result.append(sk)
    elif result[-1][1] != sk[1]:
        result.append(sk)


def skyline_merge(s1, s2):
    h1 = h2 = 0
    l1 = l2 = 0

    result = []
    while l1 < len(s1) and l2 < len(s2):
        if s1[l1][0] <= s2[l2][0]:
            h1 = s1[l1][1]
            append_skyline(result, (s1[l1][0], max(h1, h2)))
            l1 += 1
        else:
            h2 = s2[l2][1]
            append_skyline(result, (s2[l2][0], max(h1, h2)))
            l2 += 1

    while l1 < len(s1):
        result.append(s1[l1])
        l1 += 1

    while l2 < len(s2):
        result.append(s2[l2])
        l2 += 1

    return result


def skyline(buildings):
    L = len(buildings)
    if L == 1:
        left, ht, right = buildings[0]
        return [(left, ht), (right, 0)]

    mid = L/2
    s1 = skyline(buildings[:mid])
    s2 = skyline(buildings[mid:])
    return skyline_merge(s1, s2)


if __name__ == '__main__':
    buildings = [(1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16),
          (14, 3, 25), (19, 18, 22), (23, 13, 29), (24, 4, 28)]
    buildings.sort(key=lambda k: k[0])
    print(buildings)
    print(skyline(buildings))
