import random


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def bubble_sort(A):
    n = len(A)

    for i in range(n):
        for j in range(n):
            if A[i] < A[j]:
                swap(A, i, j)

if __name__ == '__main__':
    B = random.sample(range(1, 20), 10)
    print(B)
    bubble_sort(B)
    print(B)