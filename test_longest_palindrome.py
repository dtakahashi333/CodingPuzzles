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
