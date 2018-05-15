
#
# Generate all strings of n-bits
#
#  T(n) = O(2^n)


def binary(A, n):
    if n < 1:
        B = A[:]
        B.reverse()
        print(B)
    else:
        A[n-1] = 0
        binary(A, n-1)
        A[n-1] = 1
        binary(A, n-1)

#
# Generate all the strings of length n drawn from 0....k-1
#


def k_string(A, n, k):
    if n<1:
        print(A)
    else:
        for i in range(k):
            A[n-1] = i
            k_string(A, n-1, k)

if __name__ == '__main__':
    n = 4
    binary([0]*4, n)

    print('k-string')
    k_string([0]*4, n, 3)