from typing import List


# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75
class KidsWithCandies:

    @staticmethod
    def solve(candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = [False] * n
        max_num = max(candies)
        for i in range(n):
            result[i] = (candies[i] + extraCandies >= max_num)
        return result
