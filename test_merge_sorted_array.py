from unittest import TestCase
from merge_sorted_array import MergeSortedArray

class TestMergeSortedArray(TestCase):

    def test_solve1(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        expected = [1,2,2,3,5,6]
        MergeSortedArray.solve(nums1, m, nums2, n)
        self.assertEqual(expected, nums1)

    def test_solve2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        expected = [1]
        MergeSortedArray.solve(nums1, m, nums2, n)
        self.assertEqual(expected, nums1)

    def test_solve3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        expected = [1]
        MergeSortedArray.solve(nums1, m, nums2, n)
        self.assertEqual(expected, nums1)
