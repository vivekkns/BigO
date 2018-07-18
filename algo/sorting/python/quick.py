import random
import time
import sys


def partition(A, left, right):
    pi = left
    for i in xrange(left, right):
        if A[i] <= A[right]:
            A[i], A[pi] = A[pi], A[i]
            pi += 1
    A[pi], A[right] = A[right], A[pi]
    return pi


def randomized_partition(A, left, right):
    ri = random.randint(left, right)
    A[right], A[ri] = A[ri], A[right]
    return partition(A, left, right)


def quicksort(A, left, right, par_func):
    if right < left:
        return
    pi = par_func(A, left, right)
    quicksort(A, left, pi-1, par_func)
    quicksort(A, pi+1, right, par_func)


def k_th_small(A, left, right, k, par_func):
    if right < left:
        return

    pi = par_func(A, left, right)
    if pi == k-1:
        return A[pi]
    elif k-1 < pi:
        return k_th_small(A, left, pi-1, k, par_func)
    else:
        return k_th_small(A, pi+1, right, k, par_func)


def run_algo(A):
    B = A[:]
    startTime = time.time()
    quicksort(A, 0, len(A)-1, partition)
    print 'Normal', time.time() - startTime

    startTime = time.time()
    quicksort(B, 0, len(B)-1, randomized_partition)
    print 'Randomized', time.time() - startTime

    # Normal 0.0295631885529
    # Randomized 0.0487279891968


def example_random_array():
    A = random.sample(xrange(1, 1000000), 10000)
    run_algo(A)

    # Normal 8.73901391029
    # Randomized 0.0367560386658


def example_sorted_aary():
    n = 10000
    sys.setrecursionlimit(n+100)
    A = range(0, n)
    run_algo(A)

if __name__ == '__main__':
    A = random.sample(xrange(1, 15), 10)
    print(A)
    print(k_th_small(A, 0, len(A)-1, 9, partition))
    print sorted(A)
    # example_random_array()
    # example_sorted_aary()

