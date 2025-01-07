from unittest import TestCase
from median_sorted_arrays import MedianSortedArrays


class TestMedianSortedArrays(TestCase):

    def test_solve1(self):
        nums1 = [1, 3]
        nums2 = [2]
        expected = 2.00000
        self.assertAlmostEqual(expected, MedianSortedArrays.solve(nums1, nums2))

    def test_solve2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected = 2.50000
        self.assertAlmostEqual(expected, MedianSortedArrays.solve(nums1, nums2))
