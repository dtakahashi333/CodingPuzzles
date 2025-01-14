# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/
from typing import List


class LongestCommonPrefix:

    @staticmethod
    def solve(strs: List[str]) -> str:
        prefix = ""
        i = 0
        while True:
            if i > len(strs[0]) - 1:
                return prefix
            cur = strs[0][i]
            for j in range(1, len(strs)):
                if i > len(strs[j]) - 1 or strs[j][i] != cur:
                    return prefix
            prefix += cur
            i += 1

    @staticmethod
    def solveByDivideAndConquer(strs: List[str]) -> str:
        return LongestCommonPrefix.helperByDivideAndConquer(strs, 0, len(strs) - 1)

    @staticmethod
    def helperByDivideAndConquer(strs: List[str], i: int, j: int) -> str:
        if i == j:
            return strs[i]
        mid = (j + i) // 2
        return LongestCommonPrefix.LCP(
            LongestCommonPrefix.helperByDivideAndConquer(strs, i, mid),
            LongestCommonPrefix.helperByDivideAndConquer(strs, mid + 1, j)
        )

    @staticmethod
    def LCP(left: str, right: str) -> str:
        min_len = min(len(left), len(right))
        for i in range(min_len):
            if left[i] != right[i]:
                return left[:i]
        return left[:min_len]

    @staticmethod
    def solveByBinarySearch(strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        return LongestCommonPrefix.helperByBinarySearch(strs, 0, len(strs[0]) - 1)

    @staticmethod
    def helperByBinarySearch(strs: List[str], i: int, j: int) -> str:
        if i > j:
            return ""
        if i == j:  # Last one character.
            for k in range(1, len(strs)):
                if i > len(strs[k]) - 1 or strs[k][i] != strs[0][i]:
                    return ""
            return strs[0][i]
        mid = (i + j) // 2
        first = strs[0][i:mid + 1]
        for k in range(1, len(strs)):
            if mid > len(strs[k]) - 1 or strs[k][i:mid + 1] != first:
                return LongestCommonPrefix.helperByBinarySearch(strs, i, mid)
        return first + LongestCommonPrefix.helperByBinarySearch(strs, mid + 1, j)
