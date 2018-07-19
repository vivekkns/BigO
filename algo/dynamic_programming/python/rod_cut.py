def cutRod_rec(L, P, N):
    p = 0
    for l in range(len(L)):
        if N-L[l] >= 0:
            p = max(p, P[l] + cutRod_rec(L, P, N-L[l]))
    return p


def cutRod(L, P, N):
    val = [0 for _ in range(N+1)]
    for n in range(1, N+1):
        max_val = -1
        for l in range(len(L)):
            if n-L[l] >= 0:
                max_val = max(max_val, P[l] + val[n-L[l]])
        val[n] = max_val
    return val[N]

if __name__ == '__main__':
    L = [1, 2, 3, 4, 5,   6,  7,  8]
    P = [1, 5, 8, 9, 10, 17, 17, 20]

    # L = [1, 2]
    # P = [1, 5]
    N = len(L)
    print(cutRod(L, P, N))
    print(cutRod_rec(L, P, N))
