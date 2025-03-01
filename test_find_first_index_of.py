from unittest import TestCase
from find_first_index_of import FindFirstIndexOf


class TestFindFirstIndexOf(TestCase):

    def test_solve1(self):
        haystack = "sadbutsad"
        needle = "sad"
        expected = 0
        self.assertEqual(expected, FindFirstIndexOf.solve(haystack, needle))

    def test_solve2(self):
        haystack = "leetcode"
        needle = "leeto"
        expected = -1
        self.assertEqual(expected, FindFirstIndexOf.solve(haystack, needle))

    def test_solve3(self):
        haystack = "a"
        needle = "a"
        expected = 0
        self.assertEqual(expected, FindFirstIndexOf.solve(haystack, needle))

    def test_solve4(self):
        haystack = ""
        needle = ""
        expected = -1
        self.assertEqual(expected, FindFirstIndexOf.solve(haystack, needle))
