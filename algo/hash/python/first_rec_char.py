#
#  First Recurring Character
#


def first_rec_char(S):
    #
    #
    d = {}
    for c in S:
        if c in d:
            return c
        d[c] = 0
    return None


if __name__ == '__main__':
    print(first_rec_char('ABCABACC'))
    print(first_rec_char('ABCD'))
