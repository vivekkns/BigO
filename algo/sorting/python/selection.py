import random


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def selection_sort(A):
    n = len(A)
    for i in range(n):
        cur_min_pos = i
        for j in range(i, n):
            if A[j] < A[cur_min_pos]:
                cur_min_pos = j
        swap(A, i, cur_min_pos)

if __name__ == '__main__':
    B = random.sample(range(1, 20), 10)

    print('selection_sort')
    B1 = B[:]
    print('Before sorting', B1)
    selection_sort(B1)
    print('After sorting', B1)