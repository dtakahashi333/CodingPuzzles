# 27. Remove Element
# https://leetcode.com/problems/remove-element/
from typing import List


class RemoveElement:

    @classmethod
    def solve(cls, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        nums.sort()
        ind = cls.find(nums, val, 0, n - 1)
        if ind < 0:  # Not found
            return n
        # Shift the index to the maximum position.
        while ind < n and nums[ind] == val:
            ind += 1
        ind -= 1
        if ind == n - 1:
            # Calculate the number of elements which are not equal to val.
            while ind >= 0 and nums[ind] == val:
                ind -= 1
            return ind + 1
        j = n - 1  # Where the target value to be swapped.
        for k in range(ind, -1, -1):
            if nums[k] != val:
                break
            # Swap values
            tmp = nums[k]
            nums[k] = nums[j]
            nums[j] = tmp
            j -= 1
        return j + 1  # 0-based index

    @classmethod
    def find(cls, nums: List[int], val: int, i: int, j: int) -> int:
        if i > j: # Not found
            return -1
        mid = (i + j) // 2
        if nums[mid] > val:
            return cls.find(nums, val, i, mid - 1)
        elif nums[mid] < val:
            return cls.find(nums, val, mid + 1, j)
        else:  # nums[mid] == val
            return mid
