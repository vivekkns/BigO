from pprint import pprint


def LCSLen(A, i, m, B, j, n):
    if i == m or j == n:
        return 0
    if A[i] == B[j]:
        return 1 + LCSLen(A, i + 1, m, B, j + 1, n)
    else:
        return max(LCSLen(A, i + 1, m, B, j, n),
                   LCSLen(A, i, m, B, j + 1, n))


def LCSLenDP(A, m, B, n):
    tbl = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                tbl[i][j] = 0
            elif A[i-1] == B[j-1]:
                tbl[i][j] = tbl[i-1][j-1] + 1
            else:
                tbl[i][j] = max(tbl[i][j-1], tbl[i-1][j])
    pprint(tbl)
    return tbl[m][n]


def LCSDP(A, m, B, n):
    tbl = [[0 for _ in range(n+1)] for _ in range(m+1)]
    mark = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                tbl[i][j] = 0
            elif A[i-1] == B[j-1]:
                tbl[i][j] = tbl[i-1][j-1] + 1
                mark[i][j] = 'D'
            elif tbl[i-1][j] >= tbl[i][j-1]:
                tbl[i][j] = tbl[i-1][j]
                mark[i][j] = 'U'
            else:
                tbl[i][j] = tbl[i][j-1]
                mark[i][j] = 'L'

    pprint(tbl)
    pprint(mark)

    i = m
    j = n

    seq = []
    while i > 0 and j > 0:
        if mark[i][j] == 'D':
            seq.insert(0, A[i-1])
            i -= 1
            j -= 1
        elif mark[i][j] == 'U':
            i -= 1
        else:
            j -= 1

    return seq, tbl[m][n]


if __name__ == '__main__':
    A = 'ABCBDAB'
    B = 'BDCA'

    print(LCSLen(A, 0, len(A), B, 0, len(B)))
    print(LCSLenDP(A, len(A), B, len(B)))
    print(LCSDP(A, len(A), B, len(B)))
