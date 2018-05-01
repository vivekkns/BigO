
#
#  First Recurring Character
#


def first_rec_char(S):
    #
    #
    d = {}
    for c in S:
        if c in d:
            return c
        d[c] = 0
    return None

#
# All Subsets of a Set
#


def print_all_sets_iterative(L):
    for n in xrange(2 ** len(L)):
        k = 0
        S = []
        while k <= len(L):
            if n & 1:
                S.append(L[k])
            n >>= 1
            k += 1

        print S


def print_all_sets(L):
    PL = [0] * len(L)
    helper(L, PL, 0)


def helper(L, PL, i):
    if i == len(L):
        print tuple(j for j in PL if j is not None)
    else:
        PL[i] = None
        helper(L, PL, i+1)
        PL[i] = L[i]
        helper(L, PL, i+1)


if __name__ == '__main__':
    print first_rec_char('ABCABACC')
    print first_rec_char('ABCD')

    # print_all_sets([1, 2, 3])
    print_all_sets_iterative([1, 2, 3, 4])
