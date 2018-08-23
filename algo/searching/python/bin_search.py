
def first_occ(A, k):
    l = 0
    r = len(A) - 1

    if A[0] == k:
        return 0

    while l <= r:
        m = l + (r-l)/2
        if A[m] == k:
            if m == 0 or A[m-1] != k:
                return m
            else:
                r = m - 1
        elif A[m] < k:
            l = m + 1
        else:
            r = m - 1

    return -1


def first_larger_than_k(A, k):
    l = 0
    r = len(A) - 1

    if A[0] > k:
        return 0

    while l <= r:
        m = l + (r-l)/2
        if A[m] > k:
            if m == 0 or A[m-1] <= k:
                return m
            else:
                r = m - 1
        elif A[m] <= k:
            l = m + 1
        else:
            r = m - 1

    return -1

if __name__ == '__main__':
    print(first_occ([1, 2, 3, 4, 5, 6, 7], 4))
    print(first_occ([4, 4, 4, 4, 5, 6, 7], 4))
    print(first_occ([-1, 2, 4, 4, 5, 6, 7], 4))

    print(first_larger_than_k([1, 2, 3, 4, 5, 6, 7], 4))
    print(first_larger_than_k([4, 4, 4, 4, 5, 6, 7], 4))
    print(first_larger_than_k([-1, 2, 4, 4, 4, 5, 6, 7], 4))
    print(first_larger_than_k([5, 6, 7], 4))
