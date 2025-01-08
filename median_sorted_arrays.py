import sys
from typing import List


class MedianSortedArrays:

    @staticmethod
    def solve(nums1: List[int], nums2: List[int]) -> float:
        # O(m+n)
        merged = []
        while len(nums1) > 0 or len(nums2) > 0:
            if len(nums1) > 0 and len(nums2) > 0:
                if nums1[0] < nums2[0]:
                    merged.append(nums1.pop(0))
                elif nums1[0] > nums2[0]:
                    merged.append(nums2.pop(0))
                else:
                    merged.append(nums1.pop(0))
                    merged.append(nums2.pop(0))
            elif len(nums1) > 0:
                while len(nums1) > 0:
                    merged.append(nums1.pop(0))
            elif len(nums2) > 0:
                while len(nums2) > 0:
                    merged.append(nums2.pop(0))

        mid = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            return merged[mid]

    @staticmethod
    def solveByOptimal(nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        k = (n + m) // 2  # middle index of a merged array
        if (n + m) % 2 == 0:
            return (MedianSortedArrays.helperByOptimal(nums1, nums2, k - 1) + MedianSortedArrays.helperByOptimal(nums1,
                                                                                                                 nums2,
                                                                                                                 k)) / 2
        else:
            return MedianSortedArrays.helperByOptimal(nums1, nums2, k)

    @staticmethod
    def helperByOptimal(nums1: List[int], nums2: List[int], k: int) -> float:
        # head and tail indices of the first array.
        a_start = 0
        a_end = len(nums1) - 1
        # head and tail indices of the second array.
        b_start = 0
        b_end = len(nums2) - 1
        while True:
            if a_start > a_end:
                return nums2[k - a_start]
            if b_start > b_end:
                return nums1[k - b_start]

            a_mid = (a_start + a_end) // 2
            b_mid = (b_start + b_end) // 2
            if a_mid + b_mid < k:
                if nums1[a_mid] > nums2[b_mid]:
                    # k is on the right side elements.
                    b_start = b_mid + 1
                    # k -= (b_mid + 1)
                else:
                    # k is on the right side elements.
                    a_start = a_mid + 1
                    # k -= (a_mid + 1)
            else:
                if nums1[a_mid] > nums2[b_mid]:
                    # k is on the left side elements.
                    a_end = a_mid - 1  # throw away the right half of nums1.
                else:
                    # k is on the left side elements.
                    b_end = b_mid - 1  # throw away the right half of nums2.


# LeetCode Approach 2
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        na, nb = len(A), len(B)
        n = na + nb

        def solve(k, a_start, a_end, b_start, b_end):
            # If the segment of on array is empty, it means we have passed all
            # its element, just return the corresponding element in the other array.
            if a_start > a_end:
                return B[k - a_start]
            if b_start > b_end:
                return A[k - b_start]

            # Get the middle indexes and middle values of A and B.
            a_index, b_index = (a_start + a_end) // 2, (b_start + b_end) // 2
            a_value, b_value = A[a_index], B[b_index]

            # If k is in the right half of A + B, remove the smaller left half.
            if a_index + b_index < k:
                if a_value > b_value:
                    return solve(k, a_start, a_end, b_index + 1, b_end)
                else:
                    return solve(k, a_index + 1, a_end, b_start, b_end)
            # Otherwise, remove the larger right half.
            else:
                if a_value > b_value:
                    return solve(k, a_start, a_index - 1, b_start, b_end)
                else:
                    return solve(k, a_start, a_end, b_start, b_index - 1)

        if n % 2:
            return solve(n // 2, 0, na - 1, 0, nb - 1)
        else:
            return (
                    solve(n // 2 - 1, 0, na - 1, 0, nb - 1)
                    + solve(n // 2, 0, na - 1, 0, nb - 1)
            ) / 2
