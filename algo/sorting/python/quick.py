import random


def partition(A, left, right):
    pi = left
    for i in xrange(left, right):
        if A[i] <= A[right]:
            A[i], A[pi] = A[pi], A[i]
            pi += 1
    A[pi], A[right] = A[right], A[pi]
    return pi


def quicksort(A, left, right):
    if right < left:
        return
    pi = partition(A, left, right)
    quicksort(A, left, pi-1)
    quicksort(A, pi+1, right)


if __name__ == '__main__':
    A = random.sample(xrange(1, 100), 10)
    print A
    quicksort(A, 0, len(A)-1)
    print A
