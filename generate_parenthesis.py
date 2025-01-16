# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/
from typing import List


class GenerateParenthesis:

    @staticmethod
    def solve(n: int) -> List[str]:
        paren, output = [], []
        GenerateParenthesis.helper(n, n, paren, output)
        return output

    @staticmethod
    def helper(i: int, j: int, paren: List[str], output: List[str]):
        if i == 0 and j == 0:
            output.append("".join(paren))
            return

        # Open
        if i > 0:
            paren.append("(")
            GenerateParenthesis.helper(i - 1, j, paren, output)
            paren.pop()
        if j > 0 and i < j:
            # Close
            paren.append(")")
            GenerateParenthesis.helper(i, j - 1, paren, output)
            paren.pop()
