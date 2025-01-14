from unittest import TestCase
from longest_common_prefix import LongestCommonPrefix


class TestLongestCommonPrefix(TestCase):

    def test_solve(self):
        strs = ["flower", "flow", "flight"]
        expected = "fl"
        self.assertEqual(expected, LongestCommonPrefix.solve(strs))
        strs = ["dog", "racecar", "car"]
        expected = ""
        self.assertEqual(expected, LongestCommonPrefix.solve(strs))

    def test_solveByDivideAndConquer(self):
        strs = ["flower", "flow", "flight"]
        expected = "fl"
        self.assertEqual(expected, LongestCommonPrefix.solveByDivideAndConquer(strs))
        strs = ["dog", "racecar", "car"]
        expected = ""
        self.assertEqual(expected, LongestCommonPrefix.solveByDivideAndConquer(strs))

    def test_solveByBinarySearch(self):
        strs = ["flower", "flow", "flight"]
        expected = "fl"
        self.assertEqual(expected, LongestCommonPrefix.solveByBinarySearch(strs))
        strs = ["dog", "racecar", "car"]
        expected = ""
        self.assertEqual(expected, LongestCommonPrefix.solveByBinarySearch(strs))
        strs = [""]
        expected = ""
        self.assertEqual(expected, LongestCommonPrefix.solveByBinarySearch(strs))
        strs = ["a"]
        expected = "a"
        self.assertEqual(expected, LongestCommonPrefix.solveByBinarySearch(strs))
        strs = ["flower", "flower", "flower", "flower"]
        expected = "flower"
        self.assertEqual(expected, LongestCommonPrefix.solveByBinarySearch(strs))
        strs = ["", ""]
        expected = ""
        self.assertEqual(expected, LongestCommonPrefix.solveByBinarySearch(strs))
        strs = ["ab", "a"]
        expected = "a"
        self.assertEqual(expected, LongestCommonPrefix.solveByBinarySearch(strs))
