# Find all triplets with zero sum


def three_sum_n3(A):
    n = len(A)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if A[i] + A[j] + A[k] == 0:
                    print(A[i], A[j], A[k])


def three_sum_n2_hash(B):
    A = B[:]
    A.sort()
    n = len(A)

    for i in range(n-2):
        h = dict()
        for j in range(i+1, n-1):
            if -(A[i]+A[j]) in h:
                print(A[i], A[j], -(A[i]+A[j]))
            else:
                h[A[j]] = j


def two_sum_n_on_sorted_array(A):
    B = A[:]
    B.sort()
    n = len(B)

    l = 0
    r = n - 1

    while l < r:
        s = A[l] + A[r]
        if s < 0:
            l += 1
        elif s > 0:
            r -= 1
        else:
            print(A[l], A[r])
            l += 1
            r -= 1


def three_sum_n2(B):
    A = B[:]
    A.sort()
    n = len(A)
    for i in range(n-2):
        l = i+1
        r = n-1
        # find two number which are summed to -A[i]
        # in the sub-array A[i+1 ... n]
        while l < r:
            s = A[i] + A[l] + A[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                print(A[i], A[l], A[r])
                l += 1
                r -= 1
                break

if __name__ == '__main__':
    A = [-1, 0, -1, 1, 2, 4]
    print('n3 algo')
    three_sum_n3(A)

    print('n2 algo')
    three_sum_n2(A)

    print('n2 hash algo')
    three_sum_n2_hash(A)
