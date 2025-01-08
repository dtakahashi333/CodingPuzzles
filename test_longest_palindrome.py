from unittest import TestCase
from longest_palindrome import LongestPalindrome


class TestLongestPalindrome(TestCase):

    def test_solve_by_brute_force(self):
        s = "babad"
        a = ["bab", "aba"]
        self.assertIn(LongestPalindrome.solveByBruteForce(s), a)
        s = "cbbd"
        a = ["bb"]
        self.assertIn(LongestPalindrome.solveByBruteForce(s), a)
        s = "a"
        a = ["a"]
        self.assertIn(LongestPalindrome.solveByBruteForce(s), a)
        s = "ac"
        a = ["a", "c"]
        self.assertIn(LongestPalindrome.solveByBruteForce(s), a)
        s = "aacabdkacaa"
        a = ["aca"]
        self.assertIn(LongestPalindrome.solveByBruteForce(s), a)

    def test_solve_by_tabulation(self):
        s = "babad"
        a = ["bab", "aba"]
        self.assertIn(LongestPalindrome.solveByTabulation(s), a)
        s = "cbbd"
        a = ["bb"]
        self.assertIn(LongestPalindrome.solveByTabulation(s), a)
        s = "a"
        a = ["a"]
        self.assertIn(LongestPalindrome.solveByTabulation(s), a)
        s = "ac"
        a = ["a", "c"]
        self.assertIn(LongestPalindrome.solveByTabulation(s), a)
        s = "aacabdkacaa"
        a = ["aca"]
        self.assertIn(LongestPalindrome.solveByTabulation(s), a)

    def test_solve_by_center_expansion(self):
        s = "babad"
        a = ["bab", "aba"]
        self.assertIn(LongestPalindrome.solveByCenterExpansion(s), a)
        s = "cbbd"
        a = ["bb"]
        self.assertIn(LongestPalindrome.solveByCenterExpansion(s), a)
        s = "a"
        a = ["a"]
        self.assertIn(LongestPalindrome.solveByCenterExpansion(s), a)
        s = "ac"
        a = ["a", "c"]
        self.assertIn(LongestPalindrome.solveByCenterExpansion(s), a)
        s = "aacabdkacaa"
        a = ["aca"]
        self.assertIn(LongestPalindrome.solveByCenterExpansion(s), a)