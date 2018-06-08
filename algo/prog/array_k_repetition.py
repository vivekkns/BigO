
def find_k_repetition(A, k):
    d = dict()
    for a in A:
        if a in d:
            d[a] += 1
            if d[a] >= k:
                return True
        else:
            d[a] = 1
    return False


def find_k_repetition_sort(A, k):
    A.sort()

    if A is None or len(A) < 1 or k <= 0:
        raise Exception('Undefined')

    if k == 1:
        return True

    count = 1
    E = A[0]

    for i in range(1, len(A)):
        if A[i] == E:
            count += 1
            if count >= k:
                return True
        else:
            count = 1
            E = A[i]
    return False


def find_half_repetition(A):
    if A is None or len(A) < 1:
        return False

    if len(A) <= 2:
        return True

    A.sort()

    L = len(A)
    if L % 2 == 0:
        if A[L/2-1] != A[L/2]:
            if A[0] == A[L/2-1] or A[L/2] == A[L-1]:
                return True
            else:
                return False
    l = 0
    r = L/2
    e = A[r]

    while (r - l) > 1:
        m = (l+r)/2
        if A[m] == e:
            r = m
        else:
            l = m

    if A[l] == e:
        m = l
    else:
        m = r

    return A[m+L/2-1] == e

if __name__ == '__main__':
    print(find_k_repetition([1, 2, 1, 1, 2], 2))
    print(find_k_repetition_sort([1, 2, 1, 1, 1], 4))
    print(find_half_repetition([1, 1, 1, 2, 2, 2, 6]))
    print(find_half_repetition([1, 1, 2, 3]))
