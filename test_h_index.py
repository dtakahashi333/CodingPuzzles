from unittest import TestCase
from h_index import HIndex


class TestHIndex(TestCase):

    def test_solve1(self):
        citations = [3, 0, 6, 1, 5]
        expected = 3
        self.assertEqual(expected, HIndex.solve(citations))

    def test_solve2(self):
        citations = [1, 3, 1]
        expected = 1
        self.assertEqual(expected, HIndex.solve(citations))
