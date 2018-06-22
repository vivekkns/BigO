def palin_substr_brute_force(S):

    n = len(S)

    p_len = 0
    p_1 = 0
    p_2 = 0

    for i in range(n):
        for j in range(i, n):
            l = i
            r = j

            while l < r and S[l] == S[r]:
                l += 1
                r -= 1

            if l >= r:
                temp_p_len = j-i+1
                if p_len < temp_p_len:
                    p_len = temp_p_len
                    p_1 = i
                    p_2 = j
    return S[p_1:p_2+1]


def palin_substr_dynamic_prog(S):
    #
    #       0 1 2 3 4 5 6
    #       m a b c b a b
    #   0  m
    #   1  a
    #   2  b
    #   3  c
    #   4  b
    #   5  a
    #   6  b
    #

    n = len(S)
    # tbl[i][j] will be false if substring S[i..j] is not palindrome
    tbl = [[False for _ in range(n)] for _ in range(n)]

    # all substrings of length 1 are palindromes
    maxL = 1
    for i in range(n):
        tbl[i][i] = True

    start = 0
    for i in range(1, n):
        if S[i-1] == S[i]:
            tbl[i-1][i] = True
            start = i-1
            maxL = 2

    for k in range(3, n):
        for i in range(n-k+1):
            j = i + k - 1
            if tbl[i+1][j-1] and S[i] == S[j]:
                tbl[i][j] = True
                if k > maxL:
                    start = i
                    maxL = k

    return S[start:start+maxL]

if __name__ == '__main__':
    S = 'forgeeksjskeegfor'
    print(S, palin_substr_brute_force(S))
    print(S, palin_substr_dynamic_prog(S))

    S = 'AXABCBAY'
    print(S, palin_substr_brute_force(S))
    print(S, palin_substr_dynamic_prog(S))
