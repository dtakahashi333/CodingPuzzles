from unittest import TestCase
from kth_permutation import KthPermutation


class TestKthPermutation(TestCase):

    def test_solve1(self):
        n = 3
        k = 3
        expected = "213"
        self.assertEqual(expected, KthPermutation.solve(n, k))

    def test_solve2(self):
        n = 4
        k = 9
        expected = "2314"
        self.assertEqual(expected, KthPermutation.solve(n, k))

    def test_solve3(self):
        n = 3
        k = 1
        expected = "123"
        self.assertEqual(expected, KthPermutation.solve(n, k))

    def test_solve4(self):
        n = 2
        k = 2
        expected = "21"
        self.assertEqual(expected, KthPermutation.solve(n, k))
