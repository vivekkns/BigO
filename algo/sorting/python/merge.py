import random


def merge(A, L, R):
    nL = len(L)
    nR = len(R)

    l = r = a = 0

    while l < nL and r < nR:
        if L[l] <= R[r]:
            A[a] = L[l]
            a += 1
            l += 1
        else:
            A[a] = R[r]
            a += 1
            r += 1

    while l < nL:
        A[a] = L[l]
        a += 1
        l += 1

    while r < nR:
        A[a] = R[r]
        a += 1
        r += 1


def merge_sort(A):
    nA = len(A)

    if nA == 1:
        return

    mid = nA/2

    L = A[:mid]
    R = A[mid:]

    merge_sort(L)
    merge_sort(R)

    merge(A, L, R)


if __name__ == '__main__':
    A = random.sample(xrange(1, 100), 10)
    print A
    merge_sort(A)
    print A
