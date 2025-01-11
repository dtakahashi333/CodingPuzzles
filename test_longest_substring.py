from unittest import TestCase
from longest_substring import LongestSubstring


class TestLongestSubstring(TestCase):

    def test_solve_by_brute_force(self):
        input_str = ["abcabcbb", "bbbbb", "pwwkew", " ", "   "]
        a = [3, 1, 3, 1, 1]
        output = []
        for s in input_str:
            output.append(LongestSubstring.solve_by_brute_force(s))
        self.assertListEqual(a, output)

    def test_solve(self):
        input_str = ["abcabcbb", "bbbbb", "pwwkew", " ", "   "]
        a = [3, 1, 3, 1, 1]
        output = []
        for s in input_str:
            output.append(LongestSubstring.solve(s))
        self.assertListEqual(a, output)
