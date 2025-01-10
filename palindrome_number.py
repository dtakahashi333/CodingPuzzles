# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/
class PalindromeNumber:

    @staticmethod
    def solve(x: int) -> bool:
        if x < 0:
            return False
        # Convert an integer to a list of digits.
        lst = []
        while x > 0:
            lst.insert(0, x % 10)
            x = x // 10
        n = len(lst)
        for i in range(n // 2):
            if lst[i] != lst[n - i - 1]:
                return False
        return True
