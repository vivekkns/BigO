from __future__ import print_function

#
# * -> 0 or more characters
# ? -> exactly one character


def is_match_util(word, i, n, pat, j, m):
    if i == n and j == m:
        return True
    elif i == n or j == m:
        return False

    if pat[j] == '*':
        return is_match_util(word, i+1, n, pat, j, m) or \
               is_match_util(word, i+1, n, pat, j+1, m) or \
               is_match_util(word, i, n, pat, j+1, m)
    elif word[i] == pat[j] or pat[j] == '?':
        return is_match_util(word, i+1, n, pat, j+1, m)

    else:
        return False


def is_match(word, pat):
    return is_match_util(word, 0, len(word),
                         pat, 0, len(pat))


def is_match_dyn(word, pat):
    n = len(word)
    m = len(pat)

    T = [[False for _ in range(m+1)] for _ in range(n+1)]
    T[0][0] = True
    if pat[0] == '*':
        T[0][1] = True

    for i in range(1, n+1):
        for j in range(1, m+1):
            if pat[j-1] == '?' or word[i-1] == pat[j-1]:
                T[i][j] = T[i-1][j-1]
            elif pat[j-1] == '*':
                T[i][j] = T[i-1][j] or T[i][j-1]
            else:
                T[i][j] = False
    return T[n][m]

if __name__ == '__main__':
    word = 'abcdefgh'
    pat = 'a?c*g?'
    print(word, ' == ', pat, ' ?',
          'is_match:', is_match(word,pat),
          'is_match_dyn:', is_match_dyn(word, pat))
