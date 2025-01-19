from unittest import TestCase
from remove_duplicates import RemoveDuplicates


class TestRemoveDuplicates(TestCase):

    def test_solve1(self):
        nums = [1, 1, 2]
        expected_length = 2
        expected_nums = [1, 2, None]
        k = RemoveDuplicates.solve(nums)
        self.assertEqual(expected_length, k)
        for i in range(k):
            self.assertEqual(expected_nums[i], nums[i])

    def test_solve2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected_length = 5
        expected_nums = [0, 1, 2, 3, 4, None, None, None, None, None]
        k = RemoveDuplicates.solve(nums)
        self.assertEqual(expected_length, k)
        for i in range(k):
            self.assertEqual(expected_nums[i], nums[i])
