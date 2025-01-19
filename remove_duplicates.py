# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
from typing import List


class RemoveDuplicates:

    @staticmethod
    def solve(nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]
        j = 1
        for i in range(1, n):
            if nums[i] > prev:
                # swap the values.
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                prev = nums[j]
                j += 1
        return j


