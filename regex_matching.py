# 10. Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/description/
from typing import List


class RegExMatching:

    @classmethod
    def solve(cls, s: str, p: str) -> bool:
        s_list, p_list = list(s), list(p)
        s_list.append(0)
        p_list.append(0)
        return cls.helper(s_list, p_list, len(s_list) - 1, len(p_list) - 1, 0, 0)

    @classmethod
    def helper(cls, s: List[any], p: List[any], n: int, m: int, i: int, j: int) -> bool:
        # Base cases
        if s[i] == 0 and p[j] == 0:
            return True

        if p[j] == ".":
            if j + 1 < m and p[j + 1] == "*":
                for k in range(i, n + 1):
                    if cls.helper(s, p, n, m, k, j + 2):
                        return True
                return False
            elif i < n:
                return cls.helper(s, p, n, m, i + 1, j + 1)
            else:
                return False
        else:  # lowercase letter
            if j + 1 < m and p[j + 1] == "*":
                if cls.helper(s, p, n, m, i, j + 2):
                    return True
                for k in range(i, n + 1):
                    if s[k] != p[j]:
                        return False
                    if cls.helper(s, p, n, m, k + 1, j + 2):
                        return True
            elif s[i] == p[j]:
                return cls.helper(s, p, n, m, i + 1, j + 1)
            else:
                return False

    # Wrong Answer
    # @classmethod
    # def solve(cls, s: str, p: str) -> bool:
    #     n, m = len(s), len(p)
    #     dp = []
    #     for _ in range(n):
    #         dp.append([-1] * m)
    #     return cls.helper(s, p, n, m, 0, 0, dp) == 1
    #
    # @classmethod
    # def helper(cls, s: str, p: str, n: int, m: int, i: int, j: int, dp: List[List[int]]) -> int:
    #     # Base cases
    #     if i >= n and j >= m:
    #         return 1
    #     elif i < n and j >= m:
    #         return 0
    #
    #     # if dp[i][j] != -1:
    #     #     return dp[i][j]
    #
    #     is_match = 0
    #     if p[j] == ".":
    #         if j + 1 < m and p[j + 1] == "*":
    #             for k in range(i, n + 1):
    #                 if cls.helper(s, p, n, m, k, j + 2, dp) == 1:
    #                     is_match = 1
    #                     break
    #         else:
    #             is_match = cls.helper(s, p, n, m, i + 1, j + 1, dp)
    #     else:  # lowercase letter
    #         if j + 1 < m and p[j + 1] == "*":
    #             for k in range(i, n + 1):
    #                 if k > i and s[k - 1] != p[j]:
    #                     break
    #                 if cls.helper(s, p, n, m, k, j + 2, dp) == 1:
    #                     is_match = 1
    #                     break
    #         elif s[i] == p[j]:
    #             is_match = cls.helper(s, p, n, m, i + 1, j + 1, dp)
    #     dp[i][j] = is_match
    #     return is_match

    # Wrong Answer
    # @staticmethod
    # def solve(s: str, p: str) -> bool:
    #     # The regular expression cannot start with a star '*'.
    #     if p[0] == "*":
    #         return False
    #
    #     n, m = len(s), len(p)
    #     i, j = 0, 0  # i is an index for s, j is an index for p.
    #     while i < n:
    #         while j < m:
    #             if p[j] == ".":
    #                 if j + 1 < m and p[j + 1] == '*':  # repeat the same letter.
    #                     if j + 2 < m:
    #                         is_end_found = False
    #                         while i < n:
    #                             if s[i] == p[j + 2]:
    #                                 is_end_found = True
    #                             i += 1
    #                         if not is_end_found:
    #                             return False
    #                         j += 3
    #                     else:
    #                         return True
    #                 else:
    #                     i += 1
    #                     j += 1
    #             else:  # lowercase letter
    #                 if j + 1 < m and p[j + 1] == '*':  # repeat the same letter.
    #                     while i < n and s[i] == p[j]:
    #                         i += 1
    #                     j += 2  # shift the regular express including '*'.
    #                 else:  # not repeat.
    #                     if s[i] != p[j]:
    #                         return False
    #                     i += 1
    #                     j += 1  # shift the regular expression.
    #             if j < m and i >= n:
    #                 return False
    #         if i < n:
    #             return False
    #         return True
