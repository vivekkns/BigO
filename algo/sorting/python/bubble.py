import random


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def bubble_sort(A):
    n = len(A)

    for i in range(n):
        for j in range(n-1):
            if A[j+1] < A[j]:
                swap(A, j, j+1)


def bubble_sort_with_flag(A):
    n = len(A)
    for i in range(n):
        swapped = False
        for j in range(n-1):
            if A[j+1] < A[j]:
                swap(A, j+1, j)
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    B = random.sample(range(1, 20), 10)

    print('bubble_sort')
    B1 = B[:]
    print('Before sorting', B1)
    bubble_sort(B1)
    print('After sorting', B1)

    print('bubble_sort_with_flag')
    B2 = B[:]
    print('Before sorting', B2)
    bubble_sort_with_flag(B2)
    print('After sorting', B2)
