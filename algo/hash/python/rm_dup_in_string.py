

def rm_dup_n2(Sary):
    pos_no_dup = 0
    for i in range(1, len(Sary)):
        is_dup = False
        for j in range(pos_no_dup+1):
            if Sary[i] == Sary[j]:
                is_dup = True
                break
        if not is_dup:
            pos_no_dup += 1
            Sary[pos_no_dup] = Sary[i]

    for i in range(pos_no_dup+1, len(Sary)):
        Sary[i] = ''

    return Sary


def rm_dup_n2_1(Sary):
    L = len(Sary)
    i = 0
    while i < L:
        j = i + 1
        while j < L:
            if Sary[i] == Sary[j]:
                Sary[j] = Sary[L-1]
                Sary[L-1] = ''
                L -= 1
            else:
                j += 1
        i += 1
    return Sary


def rm_dup_nlgn(Sary):
    # <0 The element pointed by x goes before the element pointed by y
    # 0  The element pointed by x is equivalent to the element pointed by y
    # >0 The element pointed by x goes after the element pointed by y
    Sary.sort(lambda x, y: ord(x)-ord(y))

    L = len(Sary)
    i = 1
    last = 1
    while i < L:
        if Sary[i-1] != Sary[i]:
            if last != i:
                Sary[last] = Sary[i]
            last += 1
        i += 1
    while last < L:
        Sary[last] = ''
        last += 1

    return Sary


def rm_dup_n(Sary):
    last = 0
    d = {}
    i = 0
    while i < len(Sary):
        if Sary[i] not in d:
            d[Sary[i]] = 1
            Sary[last] = Sary[i]
            last += 1
        i += 1

    while last < len(Sary):
        Sary[last] = ''
        last += 1

    return Sary

if __name__ == '__main__':
    print(rm_dup_n2(list('ABCDABGHJ')))
    print(rm_dup_n2(list('ABCD')))

    print(rm_dup_n2_1(list('ABCDABGHJ')))
    print(rm_dup_n2_1(list('ABCD')))

    print(rm_dup_nlgn(list('ABCDABGHJ')))
    print(rm_dup_nlgn(list('ABCD')))

    print(rm_dup_n(list('ABCDABGHJ')))
    print(rm_dup_n(list('ABCD')))
