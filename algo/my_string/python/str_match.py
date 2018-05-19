

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


def rabin_karp(T, P):
    d = 256

    n = len(T)
    m = len(P)
    prime_num = 101

    hp = 0
    ht = 0

    h = 1
    for i in range(m-1):
        h = (h*d) % prime_num

    for t, p in zip(T, P):
        hp = (hp * d + ord(p)) % prime_num
        ht = (ht * d + ord(t)) % prime_num

    for i in range(n-m+1):
        if hp == ht:
            if T[i:i+m] == P:
                return True

        if i < n-m:
            ht = (d * (ht - ord(T[i])*h) + ord(T[i+m])) % prime_num

            if ht < 0:
                ht += prime_num

    return False


def prefix_table(P):
    m = len(P)
    j = 0
    i = 1
    PT = [0] * m

    while i < m:
        if P[i] == P[j]:
            PT[i] = j + 1
            j += 1
            i += 1
        elif j > 0:
            j = PT[j-1]
        else:
            PT[i] = 0
            i += 1
    return PT


def kmp(T, P):
    PT = prefix_table(P)
    n = len(T)
    m = len(P)
    i = j = 0
    while i < n:
        if T[i] == P[j]:
            if j == m-1:
                return i-j
            i += 1
            j += 1
        elif j > 0:
            j = PT[j-1]
        else:
            i += 1
    return False

if __name__ == '__main__':
    print(brute_force('ABCDFGG', 'CDF'))
    print(brute_force('ABCDFGG', 'CDDF'))

    print(rabin_karp('ABCDFGG', 'CDF'))
    print(rabin_karp('ABCDFGG', 'CDDF'))
    print(rabin_karp('CDDF', 'CDDF'))

    print(kmp('aabaabaaba', 'aabaabaaa'))
    print(kmp('abxabcabcaby', 'abcaby'))
