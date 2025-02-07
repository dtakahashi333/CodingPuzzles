from optparse import Option
from typing import List
import itertools


# 31. Next Permutation
# https://leetcode.com/problems/next-permutation/
# https://takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation/
# https://www.youtube.com/watch?v=JDOXKqF60RQ&t=1693s
class NextPermutation:

    @classmethod
    def solve(cls, nums: List[int]) -> None:
        # Get the size of a number list.
        n = len(nums)

        # nums is empty or contains a single element.
        if n <= 1:
            return

        i = n - 1
        while i >= 1 and nums[i] <= nums[i - 1]:
            i = i - 1

        if i == 0:
            # Reset nums.
            nums.sort()
        else:
            desc = nums[i:]
            desc.sort()
            j = cls.findIndex(desc, nums[i - 1], 0, len(desc) - 1)
            tmp = nums[i - 1]
            nums[i - 1] = desc[j]
            desc[j] = tmp
            for k, l in zip(range(i, n), range(0, len(desc))):
                nums[k] = desc[l]

    @classmethod
    def findIndex(cls, nums: List[int], k: int, i: int, j: int) -> (int, int):
        if i >= j:
            return i

        m = (i + j) // 2
        if nums[m] < k:
            return cls.findIndex(nums, k, m + 1, j)
        elif nums[m] > k:
            return cls.findIndex(nums, k, i, m - 1)
        else:
            return m

    @classmethod
    def printAllPermutations(cls, nums: List[int]) -> None:
        perm = itertools.permutations(nums)
        for p in perm:
            print(p)
