

def LCSLen(A, i, m, B, j, n):
    if i == m or j == n:
        return 0
    if A[i] == B[j]:
        return 1 + LCSLen(A, i + 1, m, B, j + 1, n)
    else:
        return max(LCSLen(A, i + 1, m, B, j, n),
                   LCSLen(A, i, m, B, j + 1, n))

if __name__ == '__main__':
    A = 'ABCBDAB'
    B = 'BDCABA'

    print(LCSLen(A, 0, len(A), B, 0, len(B)))
