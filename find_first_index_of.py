# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class FindFirstIndexOf:

    @classmethod
    def solve(cls, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        i, j = 0, 0  # indices of haystack and needle.
        while n - i >= m - j:
            while i < n and haystack[i] != needle[j]:
                i += 1
            if i == n:  # not match
                return -1
            first_index = i
            while i < n and j < m and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == m:  # match
                return first_index
            i = first_index + 1
            j = 0  # reset the index of needle.
        return -1
