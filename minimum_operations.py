from typing import List


# 3402. Minimum Operations to Make Columns Strictly Increasing
# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/
class MinimumOperations:

    @staticmethod
    def solve(grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        operation = 0
        for j in range(0, m):
            for i in range(1, n):
                pre = grid[i - 1][j]
                cur = grid[i][j]
                if pre >= cur:
                    operation += pre - cur + 1
                    grid[i][j] = pre + 1
        return operation
