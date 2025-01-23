from unittest import TestCase
from remove_element import RemoveElement


class TestRemoveElement(TestCase):

    def test_solve1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected = [2, 2]
        k = RemoveElement.solve(nums, val)
        self.assertEqual(k, len(expected))
        nums = sorted(nums[:k])
        for i in range(k):
            self.assertEqual(expected[i], nums[i])

    def test_solve2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected = [0, 0, 1, 3, 4]
        k = RemoveElement.solve(nums, val)
        self.assertEqual(k, len(expected))
        nums = sorted(nums[:k])
        for i in range(k):
            self.assertEqual(expected[i], nums[i])

    def test_solve3(self):
        nums = []
        val = 0
        expected = []
        k = RemoveElement.solve(nums, val)
        self.assertEqual(k, len(expected))
        nums = sorted(nums[:k])
        for i in range(k):
            self.assertEqual(expected[i], nums[i])

    def test_solve4(self):
        nums = [2]
        val = 3
        expected = [2]
        k = RemoveElement.solve(nums, val)
        self.assertEqual(k, len(expected))
        nums = sorted(nums[:k])
        for i in range(k):
            self.assertEqual(expected[i], nums[i])

    def test_solve5(self):
        nums = [2, 2, 2]
        val = 0
        expected = [2, 2, 2]
        k = RemoveElement.solve(nums, val)
        self.assertEqual(k, len(expected))
        nums = sorted(nums[:k])
        for i in range(k):
            self.assertEqual(expected[i], nums[i])
