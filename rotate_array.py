from typing import List


# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
class RotateArray:

    @classmethod
    def solveByBruteForce(cls, nums: List[int], k: int) -> None:
        n = len(nums)
        for _ in range(k):
            tmp = nums[n - 1]
            for i in range(n - 2, -1, -1):
                nums[i + 1] = nums[i]
            nums[0] = tmp

    @classmethod
    def solve(cls, nums: List[int], k: int) -> None:
        cls.helper(nums, k % len(nums), 0, len(nums) - 1)

    @classmethod
    def helper(cls, nums: List[int], k: int, i: int, j: int) -> None:
        if j - i < 1 or k == 0:
            return
        n = j - i + 1
        half = (j - i) // 2
        if k <= half:
            for l in range(k):
                tmp = nums[i + l]
                nums[i + l] = nums[j - (k - 1) + l]
                nums[j - (k - 1) + l] = tmp
            cls.helper(nums, k, i + k, j)
        else:
            for l in range(n - k):
                tmp = nums[i + l]
                nums[i + l] = nums[j - (n - k) + 1 + l]
                nums[j - (n - k) + 1 + l] = tmp
            cls.helper(nums, 2 * k - n, i, j - (n - k))
