import random


def insertion_sort(A):
    for i in xrange(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1

#
# Find a point where the new element goes using binary search
# to minimize the comparision cost
#
#
# The following function will return the index
# where the new element can go
#


def bin_search_insert_pos(A, left, right, value):
    if left == right:
        if value < A[left]:
            return left
        elif value >= A[right]:
            return right+1

    mid = (left + right)/2
    if A[mid] <= value <= A[mid+1]:
        return mid + 1
    elif value < A[mid]:
        return bin_search_insert_pos(A, left, mid, value)
    else:
        return bin_search_insert_pos(A, mid + 1, right, value)


def normal_bin_search(A, left, right, value):
    if right < left:
        return -1
    mid = (right+left) / 2
    if A[mid] == value:
        return mid
    elif value < A[mid]:
        return normal_bin_search(A, left, mid-1, value)
    else:
        return normal_bin_search(A, mid+1, right, value)


def insertion_sort_with_binary_serach(A):
    for i in xrange(1, len(A)):
        pos_to_insert = bin_search_insert_pos(A, 0, i - 1, A[i])
        temp = A[i]
        j = i
        while j > pos_to_insert:
            A[j] = A[j-1]
            j -= 1
        A[pos_to_insert] = temp

if __name__ == '__main__':

    B = random.sample(xrange(1, 10000000), 1000)
    C = B[:]

    import time
    startTime = time.time()
    insertion_sort(B)
    print time.time() - startTime

    startTime = time.time()
    insertion_sort_with_binary_serach(C)
    print time.time() - startTime

    #
    # For 10,000 random number observed
    #
    # 5.16027522087
    # 2.20832586288
    #

    print B == C
