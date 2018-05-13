

def brute_force(T, P):
    n = len(T)
    m = len(P)
    i = 0
    while i < n:
        j = 0
        while j < m and T[i+j] == P[j]:
            j += 1
        if j == m:
            return True
        i += 1
    return False

if __name__ == '__main__':
    print(brute_force('ABCDFGG', 'CDF'))
    print(brute_force('ABCDFGG', 'CDDF'))