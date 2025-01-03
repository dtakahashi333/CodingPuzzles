from typing import List


# 1. Two Sum
# https://leetcode.com/problems/two-sum/
class TwoSum:

    @staticmethod
    def solve(nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_map = {}
        for i in range(n):
            hash_map[nums[i]] = i
        for i in range(n):
            key = target - nums[i]
            if key in hash_map and hash_map[key] != i:
                return [i, hash_map[key]]
        return []
