from unittest import TestCase
from length_of_longest_substring import LengthOfLongestSubstring


class TestLengthOfLongestSubstring(TestCase):

    def test_solve_by_brute_force(self):
        input_str = ["abcabcbb", "bbbbb", "pwwkew", " ", "   "]
        a = [3, 1, 3, 1, 1]
        output = []
        for s in input_str:
            output.append(LengthOfLongestSubstring.solve_by_brute_force(s))
        self.assertListEqual(a, output)

    def test_solve(self):
        input_str = ["abcabcbb", "bbbbb", "pwwkew", " ", "   "]
        a = [3, 1, 3, 1, 1]
        output = []
        for s in input_str:
            output.append(LengthOfLongestSubstring.solve(s))
        self.assertListEqual(a, output)
