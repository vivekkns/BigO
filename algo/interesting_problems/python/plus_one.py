# Add One To Number
#


def plusOne(A):
    L = [0]
    L.extend(A)
    i = len(A)

    while L[i] == 9:
        L[i] = 0
        i -= 1
    L[i] += 1

    i = 0
    while not L[i]:
        i += 1

    return L[i:]


if __name__ == '__main__':
    print(plusOne([0, 0, 4, 5, 9, 9, 9]))
