from __future__ import print_function

#
# Finding missing and duplicate elements in an array
#
# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except D which appears twice and M which is missing.

#
# method-1
#
#  1+2+3...n = n(n+1)/2
#  sum(A)+ M - D = n(n+1)/2
#  sum(A.A) + M**2 - D**2 = n(n+1)(2n+1)/6
#


def findMissDup(A):
    n = len(A)
    m_minus_d = n*(n+1)/2 - sum(A)
    m_plus_d = (n*(n+1)*(2*n+1)/6 - sum(i*i for i in A))/m_minus_d

    m = (m_minus_d + m_plus_d) / 2
    d = m_plus_d - m

    return m, d

#
# method - 2
# x ^ x = 0
# x ^ x ^ x = x
#
# x ^ y = a
# if any bit is set in a bit position,
# it must be either from x or y
#
# 1 2 3 4 2 6
# 1 2 3 4 5 6
#


def findMissDup_bit(A):
    x = 0
    for i, a in enumerate(A, 1):
        x ^= i ^ a

    #
    # Now x = m ^ d
    # let k be any bit set in x
    #

    # x         = 1010100
    # x-1       = 1010011
    # ~(x-1)    = 0101100
    # x & ~(x-1)= 0000100

    k = x & ~(x - 1)

    d = 0

    #
    # Now, xor all the numbers that have this kth bit set
    #
    for i, a in enumerate(A, 1):
        if i & k:
            d ^= i
        if a & k:
            d ^= a

    return x ^ d, d


def find_set_bit_pos(n):
    """
    Find position of the only set bit
    """
    c = 0
    while n:
        c += 1
        n >>= 1
    return c


def count_set_bits(n):
    """
    count of set bits
    """
    c = 0
    while n:
        c += n & 1
        n >>= 1
    return c


def count_all_bits_n_1(n):
    total_bits = 0
    for num in range(1, n+1):
        total_bits += count_set_bits(num)
    return total_bits


def count_all_bits_n_2(n):
    pass


def main():

    print('find_set_bit(16) = ', find_set_bit_pos(16))
    print('count_set_bits(5) = ', count_set_bits(5))
    print('count_all_bits_n_1(5) = ', count_all_bits_n_1(5))

    A = [1, 2, 3, 6, 5, 2]
    print('findMissDup of     ', A, ' = ', findMissDup(A))
    print('findMissDup_bit of ', A, ' = ', findMissDup_bit(A))

    A = [1, 2, 3, 4, 3, 6]
    print('findMissDup_bit of ', A, ' = ', findMissDup_bit(A))

if __name__ == '__main__':
    main()

