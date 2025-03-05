from random import shuffle
from typing import List


# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150
class ProductExceptSelf:

    @classmethod
    def solve1(cls, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            suffix[n - i - 1] = suffix[n - i] * nums[n - i]
        result = [0] * n
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        return result

    @classmethod
    def solve2(cls, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        k = n // 2
        prefix, suffix = 1, 1
        for i in range(n):
            if i < k:
                result[i] = prefix
                result[n - 1 - i] = suffix
            else:
                result[i] *= prefix
                result[n - 1 - i] *= suffix
            prefix *= nums[i]
            suffix *= nums[n - 1 - i]
        return result
