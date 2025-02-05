from unittest import TestCase
from permutations import Permutations


class TestPermutations(TestCase):

    def test_solve_1(self):
        nums = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertListEqual(expected, Permutations.solve(nums))

    def test_solve_2(self):
        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        self.assertListEqual(expected, Permutations.solve(nums))

    def test_solve_3(self):
        nums = [1]
        expected = [[1]]
        self.assertListEqual(expected, Permutations.solve(nums))

    def test_solve2_1(self):
        nums = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertCountEqual(expected, Permutations.solve2(nums))

    def test_solve2_2(self):
        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        self.assertCountEqual(expected, Permutations.solve2(nums))

    def test_solve2_3(self):
        nums = [1]
        expected = [[1]]
        self.assertCountEqual(expected, Permutations.solve2(nums))
