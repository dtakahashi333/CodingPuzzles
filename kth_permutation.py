import math
from typing import List


# 60. Permutation Sequence
# https://leetcode.com/problems/permutation-sequence/description/
# https://takeuforward.org/data-structure/find-k-th-permutation-sequence/
# https://www.youtube.com/watch?v=wT7gcXLYoao
class KthPermutation:

    @classmethod
    def solve(cls, n: int, k: int) -> str:
        nums = []
        for i in range(1, n + 1):
            nums.append(i)
        return cls.helper(nums, n, k - 1)  # k-1 to convert the 0-based index

    @classmethod
    def helper(cls, nums: List[int], n: int, k: int) -> str:
        if n == 0:
            return ""
        fact = math.factorial(n - 1)
        # Calculate the index of the first number of the permutation.
        ind = k // fact
        s = str(nums[ind])
        nums.pop(ind)
        return s + cls.helper(nums, n - 1, k % fact)
