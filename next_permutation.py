from typing import List
import itertools


# 31. Next Permutation
# https://leetcode.com/problems/next-permutation/
# https://www.naukri.com/code360/problems/893046?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTabValue=SUBMISSION
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
            tail = sorted(nums[i:])
            for k, l in zip(range(i, n), range(len(tail))):
                nums[k] = tail[l]
            j = cls.findIndex(nums, nums[i - 1], i, n - 1)
            tmp = nums[j]
            nums[j] = nums[i - 1]
            nums[i - 1] = tmp

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
