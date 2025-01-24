from typing import List


# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/
class MostWater:

    @staticmethod
    def solveByBruteForce(height: List[int]) -> int:
        n = len(height)
        max_area = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                area = (j - i) * min(height[i], height[j])
                if area > max_area:
                    max_area = area
        return max_area

    # @staticmethod
    # def solve(height: List[int]) -> int:
    #     n = len(height)
    #     max_area = (n - 1) * min(height[0], height[n - 1])
    #     prev_max_area = max_area
    #     i, j = 0, n - 1
    #     max_i, max_j = i, j
    #     while True:
    #         while i < j:
    #             area = (j - i) * min(height[i], height[j])
    #             if area > max_area:
    #                 max_area = area
    #                 max_i = i
    #                 break
    #             i += 1
    #         i = max_i
    #         while i < j:
    #             area = (j - i) * min(height[i], height[j])
    #             if area > max_area:
    #                 max_area = area
    #                 max_j = j
    #                 break
    #             j -= 1
    #         j = max_j
    #         if max_area == prev_max_area:
    #             break
    #         prev_max_area = max_area
    #     return max_area

    # The wall heights must increase when moving the index inward from either side.
    # This is because the container's width decreases, the wall heights must ascend from
    # both ends in order to maximize the volume. Additionally, the volume is constrained
    # by the shorter of the two walls. Therefore, once one wall becomes taller than the
    # other, move the index of the shorter wall to increase the capacity, until once again
    # the height become taller than the other. Continue this operation until
    # the both indices meets at the same point.
    @staticmethod
    def solve(height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        max_area = 0
        prev_max_area = max_area
        while i < j:
            while i < j:
                area = (j - i) * min(height[i], height[j])
                if area > max_area:
                    max_area = area
                if height[i] > height[j]:
                    break
                i += 1
            while i < j:
                area = (j - i) * min(height[i], height[j])
                if area > max_area:
                    max_area = area
                if height[i] < height[j]:
                    break
                j -= 1
            if prev_max_area == max_area:
                break
            prev_max_area = max_area
        return max_area
