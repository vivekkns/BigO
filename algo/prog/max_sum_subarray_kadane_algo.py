#
# maximum sub-array
#


def max_subarray_brute_force(A):
    L = len(A)
    max_so_far = A[0]
    for i in range(L):
        for j in range(i, L):
            max_so_far = max(max_so_far, sum(A[i:j+1]))

    return max_so_far

#
# Kadane's Algorithm
#
# Suppose A[1..N] is your array for which you want to find maximum sum sub-array.
# Construct B[1..N] such that B[j]=max(Sum A[k]|k<=j,k>=i)
# (i is some starting index for which B[j] is maximum).
# So it boils down to B[j]=max(B[j-1]+A[j],A[j])
# (here I am assuming that empty sub-array isn't allowed in answer).
# And then find the maximum B[j] for all j E [1..N].
# Now this can be done in constant space since we only need result of
# the previous iteration( for j we need only B[j-1]) and the maximum sub-array sum
# which has occurred till now.
#
# A = -2, -3, 4, -1, -2, 1, 5, -3
# B = -2, -2, 4,  3,  1, 2, 7, 4
#


def max_subarray1(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    i1 = i2 = 0
    for i, a in enumerate(A[1:], 1):
        if (max_ending_here + a) >= a:
            max_ending_here = max_ending_here + a
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                i2 = i
        else:
            max_ending_here = a
            if max_ending_here >= max_so_far:
                max_so_far = max_ending_here
                i1 = i2 = i
    return max_so_far, A[i1:i2+1]


if __name__ == '__main__':
    A = [-2, -3, 4, -1, -2, 1, 5, -3]
    # A = [-3, -7, -9, -10, -1, -23]
    # A = [1, 2, 3, 4, 5]
    print(A, max_subarray_brute_force(A), max_subarray1(A), max_subarray(A))
