

def segregate(ary):
    j = 0

    for i in range(len(ary)):
        if ary[i] <= 0:
            ary[i], ary[j] = ary[j], ary[i]
            j += 1

    return j


def find_missing_positive(ary):
    for i in range(len(ary)):
        ai = abs(ary[i] - 1)
        if ai < len(ary) and ary[ai] > 0:
            ary[ai] = -ary[ai]

    for i in range(len(ary)):
        if ary[i] > 0:
            return i + 1

    return len(ary) + 1


if __name__ == '__main__':
    ary = [2, 4, -7, 6, 3, 1, -10, 5]
    pi = segregate(ary)
    print(ary, pi)
    if pi <= len(ary):
        print(ary, find_missing_positive(ary[pi:]))

