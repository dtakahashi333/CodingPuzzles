from unittest import TestCase
from median_sorted_arrays import MedianSortedArrays, Solution


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

    def test_solve_by_optimal1(self):
        nums1 = [1, 3]
        nums2 = [2]
        expected = 2.00000
        self.assertAlmostEqual(expected, MedianSortedArrays.solveByOptimal(nums1, nums2))

    def test_solve_by_optimal2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected = 2.50000
        self.assertAlmostEqual(expected, MedianSortedArrays.solveByOptimal(nums1, nums2))

    def test_solve_by_optimal3(self):
        nums1 = [1, 3, 5, 7, 9, 11]
        nums2 = [2, 4, 6, 8, 10]
        expected = 6.00000
        self.assertAlmostEqual(expected, MedianSortedArrays.solveByOptimal(nums1, nums2))


class TestSolution(TestCase):

    def test_solve(self):
        nums1 = [1, 3, 5, 7, 9, 11]
        nums2 = [2, 4, 6, 8, 10]
        expected = 6.00000
        s = Solution()
        self.assertAlmostEqual(expected, s.findMedianSortedArrays(nums1, nums2))
