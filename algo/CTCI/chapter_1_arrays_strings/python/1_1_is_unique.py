import unittest

#
# 1.1 Implement an algorithm to determine if a string has all unique characters
#

# using hash table
def is_unique_hash(S):
    tbl = dict()
    for c in S:
        if c in tbl:
            return False
        else:
            tbl[c] = 1
    return True


class test_is_unique(unittest.TestCase):
    def test_is_unique_hash(self):
        self.assertTrue(is_unique_hash('abc'))
        self.assertFalse(is_unique_hash('abb'))
        self.assertTrue(is_unique_hash('a'))
        self.assertTrue(is_unique_hash(''))

if __name__ == '__main__':
    # print(is_palindrome_permutation('a'))
    unittest.main()