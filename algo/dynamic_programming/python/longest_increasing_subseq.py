
# Longest Increasing Sub sequence

# Let arr[0..n-1] be the input array and L(i) be the length of the
# LIS ending at index i such that arr[i] is the last element of the LIS.
# Then, L(i) can be recursively written as:
# L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
# L(i) = 1, if no such j exists.
# To find the LIS for a given array,
# we need to return max(L(i)) where 0 < i < n.


def LIS(A):
    n = len(A)
    lis = [1] * n
    pos = [-1 for i in range(n)]

    for i in range(1, n):
        for j in range(0, i):
            # LCS at i is at least LCS at j plus 1
            if A[j] < A[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1
                pos[i] = j
    m = max(lis)
    p = lis.index(m)
    seq = []

    while p >= 0:
        seq.insert(0, A[p])
        p = pos[p]

    return m, seq


if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print "LIS = ", LIS(arr)
