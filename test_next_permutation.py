from unittest import TestCase
from next_permutation import NextPermutation
import itertools


class TestNextPermutation(TestCase):

    def test_solve1(self):
        nums = [1, 2, 3]
        expected = [1, 3, 2]
        NextPermutation.solve(nums)
        self.assertListEqual(expected, nums)

    def test_solve2(self):
        nums = [3, 2, 1]
        expected = [1, 2, 3]
        NextPermutation.solve(nums)
        self.assertListEqual(expected, nums)

    def test_solve3(self):
        nums = [1, 1, 5]
        expected = [1, 5, 1]
        NextPermutation.solve(nums)
        self.assertListEqual(expected, nums)

    def test_solve4(self):
        # print(list(itertools.permutations([1, 5, 5])))
        nums = [1, 5, 5]
        expected = [5, 1, 5]
        NextPermutation.solve(nums)
        self.assertListEqual(expected, nums)

    def test_solve5(self):
        nums = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 5, 4]
        NextPermutation.solve(nums)
        self.assertListEqual(expected, nums)

    def test_solve6(self):
        nums = [1]
        expected = [1]
        NextPermutation.solve(nums)
        self.assertListEqual(expected, nums)

    def test_solve7(self):
        nums = [4, 3, 2, 1]
        expected = [1, 2, 3, 4]
        NextPermutation.solve(nums)
        self.assertListEqual(expected, nums)

    def test_solve8(self):
        nums = [2, 1, 3, 4]
        expected = [2, 1, 4, 3]
        NextPermutation.solve(nums)
        self.assertListEqual(expected, nums)

    def test_solve9(self):
        nums = [1, 3, 2]
        expected = [2, 1, 3]
        NextPermutation.solve(nums)
        self.assertListEqual(expected, nums)
