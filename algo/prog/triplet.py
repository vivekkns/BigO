import sys

# Find a sorted sub sequence of size 3 in linear time

# Given an array of n integers, find the 3 elements such that
# a[i] < a[j] < a[k] and i < j < k in 0(n) time.
# If there are multiple such triplets, then print any one of them.

INF = sys.maxint


def find3subseq(A):
    L = len(A)
    lesser = [0] * L

    min = 0
    lesser[0] = -1
    for i in range(1, L):
        if A[i] <= A[min]:
            min = i
            lesser[i] = -1
        else:
            lesser[i] = min

    # [0,  1,  2,   3, 4, 5, 6 ]
    # [12, 11, 10,  5, 6, 2, 30]
    # [-1, -1, -1, -1, 3, -1, 5]

    greater = [0] * L
    max = L-1
    greater[max] = -1
    for j in range(L-2, -1, -1):
        if A[j] >= A[max]:
            greater[j] = -1
            max = j
        else:
            greater[j] = max

    # [0,  1,  2,   3, 4, 5, 6 ]
    # [12, 11, 10,  5, 6, 2, 30]
    # [6,  6,  6,   6, 6, 6, -1]

    for i in range(0, L):
        if lesser[i] != -1 and greater[i] != -1:
            return A[lesser[i]], A[i], A[greater[i]]


# O(n2)
def find3subseq_n2(A):
    L = len(A)
    pos = 0
    for i in range(L):
        flag, min1, min2 = findpair(A, pos, i)
        if flag:
            for j in range(min2+1, L):
                if A[j] > A[min2]:
                    return A[min1], A[min2], A[j]


def findpair(A, left, right):
    min = left
    for i in range(left+1, right+1):
        if A[i] > A[min]:
            return True, min, i
        else:
            min = i
    return False, min, min


if __name__ == '__main__':
    A = [12, 11, 10, 5, 6, 2, 30]
    print(find3subseq(A))
    print(find3subseq_n2(A))
