from typing import List


# 274. H-Index
# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150
class HIndex:

    @classmethod
    def solve(cls, citations: List[int]) -> int:
        n = len(citations)
        citations.sort(reverse=True)
        count = 0
        for i in range(n):
            if citations[i] < i + 1:
                break
            count += 1
        return count
