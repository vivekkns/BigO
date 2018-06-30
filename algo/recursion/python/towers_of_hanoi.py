

def towers_of_hanoi(n, from_peg, to_peg, aux_peg):
    if n == 1:
        print('Move disk 1 from peg %s to peg %s' % (from_peg, to_peg))
        return

    towers_of_hanoi(n-1, from_peg, aux_peg, to_peg)
    print('Move disk %d from peg %s to peg %s' % (n, from_peg, to_peg))

    towers_of_hanoi(n-1, aux_peg, to_peg, from_peg)


if __name__ == '__main__':
    towers_of_hanoi(3, 'A', 'B', 'C')
