
# Given n non-negative integers representing an elevation map
# where the width of each bar is 1,
# compute how much water it is able to trap after raining
#
from __future__ import print_function


def trap_water(A):
    """
    S: O(n)
    T: O(n)
    """
    n = len(A)

    left = [0] * n
    right = [0] * n

    left[0] = A[0]
    for i in range(1, n):
        left[i] = max(left[i-1], A[i])

    right[n-1] = A[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], A[i])

    water = 0

    for i in range(n):
        water += min(left[i], right[i]) - A[i]

    return water


def trap_water_space_efficient(A):
    """
    S: O(1)
    T: O(n)
    """
    n = len(A)
    water = 0

    left_max = 0
    right_max = 0

    left = 0
    right = n-1

    while left <= right:
        if A[left] < A[right]:
            if A[left] > left_max:
                left_max = A[left]
            else:
                water += left_max - A[left]
            left += 1
        else:
            if A[right] > right_max:
                right_max = A[right]
            else:
                water += right_max - A[right]
            right -= 1
    return water

if __name__ == '__main__':
    A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(A, 'Water = ', trap_water(A))
    print(A, 'Water = ', trap_water_space_efficient(A))
