from unittest import TestCase
from regex_matching import RegExMatching


class TestRegExMatching(TestCase):

    def test_solve1(self):
        s = "aa"
        p = "a"
        expected = False
        self.assertEqual(expected, RegExMatching.solve(s, p))

    def test_solve2(self):
        s = "aa"
        p = "a*"
        expected = True
        self.assertEqual(expected, RegExMatching.solve(s, p))

    def test_solve3(self):
        s = "ab"
        p = ".*"
        expected = True
        self.assertEqual(expected, RegExMatching.solve(s, p))

    def test_solve4(self):
        s = "aab"
        p = "c*a*b"
        expected = True
        self.assertEqual(expected, RegExMatching.solve(s, p))

    def test_solve5(self):
        s = "aaa"
        p = "aaaa"
        expected = False
        self.assertEqual(expected, RegExMatching.solve(s, p))

    def test_solve6(self):
        s = "mississippi"
        p = "mis*is*p*."
        expected = False
        self.assertEqual(expected, RegExMatching.solve(s, p))

    def test_solve7(self):
        s = "a"
        p = "ab*"
        expected = True
        self.assertEqual(expected, RegExMatching.solve(s, p))

    def test_solve8(self):
        s = "abcaaaaaaabaabcabac"
        p = ".*ab.a.*a*a*.*b*b*"
        expected = True
        self.assertEqual(expected, RegExMatching.solve(s, p))

    def test_solve9(self):
        s = "a"
        p = ".*..a*"
        expected = False
        self.assertEqual(expected, RegExMatching.solve(s, p))
