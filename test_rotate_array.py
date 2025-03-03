from unittest import TestCase
from rotate_array import RotateArray


class TestRotateArray(TestCase):

    def test_solveByBruteForce1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected = [5, 6, 7, 1, 2, 3, 4]
        RotateArray.solveByBruteForce(nums, k)
        self.assertListEqual(expected, nums)

    def test_solveByBruteForce2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        expected = [3, 99, -1, -100]
        RotateArray.solveByBruteForce(nums, k)
        self.assertListEqual(expected, nums)

    def test_solve1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected = [5, 6, 7, 1, 2, 3, 4]
        RotateArray.solve(nums, k)
        self.assertListEqual(expected, nums)

    def test_solve2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        expected = [3, 99, -1, -100]
        RotateArray.solve(nums, k)
        self.assertListEqual(expected, nums)

    def test_solve3(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 5
        expected = [3, 4, 5, 6, 7, 1, 2]
        RotateArray.solve(nums, k)
        self.assertListEqual(expected, nums)

    def test_solve4(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        k = 5
        expected = [5, 6, 7, 8, 9, 1, 2, 3, 4]
        RotateArray.solve(nums, k)
        self.assertListEqual(expected, nums)

    def test_solve5(self):
        nums = [1, 2]
        k = 2
        expected = [1, 2]
        RotateArray.solve(nums, k)
        self.assertListEqual(expected, nums)

    def test_solve6(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
        k = 38
        expected = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        RotateArray.solve(nums, k)
        self.assertListEqual(expected, nums)

    # def test_solve7(self):
    #     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    #     k = 54944
    #     expected = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    #     RotateArray.solve(nums, k)
    #     self.assertListEqual(expected, nums)
