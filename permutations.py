from sys import flags
from typing import List


# 46. Permutations
# https://leetcode.com/problems/permutations/description/
# https://takeuforward.org/data-structure/print-all-permutations-of-a-string-array/
# https://www.youtube.com/watch?v=YK78FU5Ffjw
# https://www.youtube.com/watch?v=f2ic2Rsc9pU
class Permutations:

    @classmethod
    def solve(cls, nums: List[int]) -> List[List[int]]:
        st, output = [], []
        for cur in nums:
            cls.helper(nums, cur, st, output)
        return output

    @classmethod
    def helper(cls, nums: List[int], cur: int, st: List[int], output: List[List[int]]) -> None:
        st.append(cur)

        count = 0
        for val in nums:
            if val not in st:
                cls.helper(nums, val, st, output)
                count += 1

        if count == 0:
            # This is the last item.
            output.append(st.copy())

        # Remove the current item.
        st.pop()
