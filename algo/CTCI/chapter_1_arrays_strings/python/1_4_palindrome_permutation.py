import unittest

#
# 1.4 Given a string, write a function to check it it a permutation of a palindrome
#


def is_palindrome_permutation(S):
    if len(S) <= 1:
        return True

    # O(n) additional space
    L = list(S)

    # By sorting
    # O(nlogn)
    L.sort()

    count = 1
    prev_char = L[0]
    char_single_occur = False
    for i in range(1, len(L)):
        if L[i] == prev_char:
            count += 1
        else:
            if count % 2:
                if char_single_occur:
                    return False
                char_single_occur = True
            count = 1
            prev_char = L[i]

    if count % 2 and char_single_occur:
        return False

    return True


# O(n) implementation
def is_palindrome_permutation_hash(S):
    tbl = dict()
    for c in S:
        if c in tbl:
            tbl[c] += 1
        else:
            tbl[c] = 1

    char_single_occur = False
    for count in tbl.values():
        if count % 2:
            if char_single_occur:
                return False
            char_single_occur = True
    return True


class palindrom_test(unittest.TestCase):
    def test_is_palindrome_permutation(self):
        self.assertTrue(is_palindrome_permutation('ababa'))
        self.assertFalse(is_palindrome_permutation('abajba'))
        self.assertTrue(is_palindrome_permutation('aaa'))
        self.assertTrue(is_palindrome_permutation('aak'))

        self.assertTrue(is_palindrome_permutation_hash('ababa'))
        self.assertFalse(is_palindrome_permutation_hash('abajba'))
        self.assertTrue(is_palindrome_permutation_hash('aaa'))
        self.assertTrue(is_palindrome_permutation_hash('aak'))

if __name__ == '__main__':
    # print(is_palindrome_permutation('a'))
    unittest.main()