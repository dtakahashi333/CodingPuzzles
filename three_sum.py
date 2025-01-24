from typing import List
from two_sum import TwoSum


# 15. 3Sum
# https://leetcode.com/problems/3sum/
class ThreeSum:

    @staticmethod
    def solveByBruteForce(nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if i != j and j != k and k != i:
                        if nums[i] + nums[j] + nums[k] == 0:
                            triplet = sorted([nums[i], nums[j], nums[k]])
                            if triplet not in result:
                                result.append(triplet)
        return result

    @staticmethod
    def solveByHashtable(nums: List[int]) -> List[List[int]]:
        pos = [0] * 100000
        neg = [0] * 100000
        for n in nums:
            if n < 0:
                neg[-n] += 1
            else:
                pos[n] += 1

        result = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                two_sum = nums[i] + nums[j]
                if abs(two_sum) < 100000:
                    third_num = -(0 + two_sum)
                    if third_num < 0:
                        if neg[-third_num] == 0:
                            continue
                        if (nums[i] == third_num and nums[j] == third_num) and neg[-third_num] == 2:
                            # The number is used.
                            continue
                        if (nums[i] == third_num or nums[j] == third_num) and neg[-third_num] == 1:
                            # The number is used.
                            continue
                    else:  # third_num >= 0
                        if pos[third_num] == 0:
                            continue
                        if (nums[i] == third_num and nums[j] == third_num) and pos[third_num] == 2:
                            # The number is used.
                            continue
                        if (nums[i] == third_num or nums[j] == third_num) and pos[third_num] == 1:
                            # The number is used.
                            continue
                    triplet = sorted([nums[i], nums[j], third_num])
                    if triplet not in result:
                        result.append(triplet)
        return result

    @staticmethod
    def solveByHashtable2(nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            target = 0 - nums[i]
            # Use a TwoSum solution.
            for j in range(len(nums)):
                inds = TwoSum.solve(nums, target)
                if len(inds) > 0 and i not in inds:
                    triplet = sorted([nums[i]] + [nums[k] for k in inds])
                    if triplet not in result:
                        result.append(triplet)
        return result

    @staticmethod
    def solveByOptimal(nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        i, j, k = 0, 1, n - 1
        result = set()
        while True:
            sum_of_three = nums[i] + nums[j] + nums[k]
            if sum_of_three < 0:
                # Move j to the next value.
                j += 1
            elif sum_of_three > 0:
                # Move k to the previous value.
                k -= 1
            else:  # sum_of_three == 0
                result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                # Move both j and k.
                j, k = j + 1, k - 1

            if j >= k:
                # Move i to the next value.
                prev = nums[i]
                while i < n and nums[i] == prev:
                    i += 1
                j, k = i + 1, n - 1
            if i >= n - 2:
                # Finish
                break
        return [list(triplet) for triplet in result]
