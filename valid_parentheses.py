# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
class ValidParentheses:

    @staticmethod
    def solve(s: str) -> bool:
        parent = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c == ")" or c == "}" or c == "]":
                if not stack:
                    return False
                if stack.pop() != parent[c]:
                    return False
            elif c == "(" or c == "{" or c == "[":
                stack.append(c)

        return not stack
