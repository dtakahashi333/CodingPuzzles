# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/
class ReverseInteger:

    @staticmethod
    def reverse_integer(x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= -1  # Make x positive.

        y = 0
        while x > 0:
            ld = x % 10  # Get the least digit.
            y = y * 10 + ld
            x //= 10

        result = sign * y
        if -pow(2, 31) <= result <= pow(2, 31) - 1:
            return result
        else:
            return 0
