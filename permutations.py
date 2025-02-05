from sys import flags
from typing import List


# 46. Permutations
# https://leetcode.com/problems/permutations/description/
# https://takeuforward.org/data-structure/print-all-permutations-of-a-string-array/
# https://www.youtube.com/watch?v=YK78FU5Ffjw
# https://www.youtube.com/watch?v=f2ic2Rsc9pU
class Permutations:

    @classmethod
    def solve(cls, nums: List[int]) -> List[List[int]]:
        st, output = [], []
        cls.helper(nums, st, output)
        return output

    @classmethod
    def helper(cls, nums: List[int], st: List[int], output: List[List[int]]) -> None:
        if len(st) == len(nums):
            output.append(st.copy())
            return

        for val in nums:
            if val not in st:
                st.append(val)
                cls.helper(nums, st, output)
                st.pop()

    #
    # The algorithm does not generate lexicographically ordered permutations.
    #
    @classmethod
    def solve2(cls, nums: List[int]) -> List[List[int]]:
        output = []
        cls.helper2(nums, 0, output)
        return output

    @classmethod
    def helper2(cls, nums: List[int], k: int, output: List[List[int]]):
        n = len(nums)

        if k == n - 1:
            output.append(nums.copy())
            return

        for i in range(k, n):
            # Swap
            tmp = nums[i]
            nums[i] = nums[k]
            nums[k] = tmp
            cls.helper2(nums, k + 1, output)
            # Roll back
            tmp = nums[i]
            nums[i] = nums[k]
            nums[k] = tmp
