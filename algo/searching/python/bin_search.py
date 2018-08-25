
# Variants of Binary Search
# 1) Contains
# 2) Index of first occurrence of a key
# 3) Index of last occurrence of a key
# 4) Index of least element greater than key
# 5) Index of greatest element less than key


def bin_search_contains(A, k):
    l = 0
    r = len(A) - 1

    result = -1
    while l <= r:
        m = l + (r-l)/2
        if A[m] == k:
            result = m
            break
        elif A[m] < k:
            l = m + 1
        else:
            r = m - 1
    return result


def bin_search_first_occurance(A, k):
    l = 0
    r = len(A) - 1

    result = -1
    while l <= r:
        m = l + (r-l)/2
        if A[m] == k:
            result = m
            r = m - 1
        elif A[m] < k:
            l = m + 1
        else:
            r = m - 1
    return result


def bin_search_last_occurance(A, k):
    l = 0
    r = len(A) - 1

    result = -1
    while l <= r:
        m = l + (r-l)/2
        if A[m] == k:
            result = m
            l = m + 1
        elif A[m] < k:
            l = m + 1
        else:
            r = m - 1
    return result


def bin_search_least_greater(A, k):
    l = 0
    r = len(A) - 1

    result = -1
    while l <= r:
        m = l + (r-l)/2
        if A[m] > k:
            result = m
            r = m - 1
        else:
            l = m + 1

    return result


def bin_search_greater_less(A, k):
    l = 0
    r = len(A) - 1

    result = -1
    while l <= r:
        m = l + (r-l)/2
        if A[m] < k:
            result = m
            l = m + 1
        else:
            r = m - 1

    return result


if __name__ == '__main__':
    print(bin_search_contains([1, 2, 3, 4, 5, 6, 7], 4))
    print(bin_search_first_occurance([4, 4, 4, 4, 5, 6, 7], 4))
    print(bin_search_last_occurance([-1, 2, 4, 4, 5, 6, 7], 4))
    print(bin_search_least_greater([1, 2, 3, 4, 5, 6, 7], 4))
    print(bin_search_greater_less([4, 4, 4, 4, 5, 6, 7], 4))
    print(bin_search_greater_less([-1, 2, 4, 4, 5, 6, 7], 4))
