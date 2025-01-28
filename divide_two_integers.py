# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/
class DivideTwoIntegers:

    @classmethod
    def solve(cls, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        sign = 1
        if dividend < 0:
            sign = ~sign + 1
            dividend = ~dividend + 1
        if divisor < 0:
            sign = ~sign + 1
            divisor = ~divisor + 1
        quotient = cls.long_division(dividend, divisor)
        if sign < 0:
            return ~quotient + 1  # To make the value negative
        else:
            return min(quotient, 2 ** 31 - 1)  # 2147483647 (32-bit integer-maximum)

    @classmethod
    def long_division(cls, dividend: int, divisor: int) -> int:
        quotient = 0
        remainder = 0
        for i in range(31, -1, -1):
            remainder = remainder << 1
            remainder = remainder | ((dividend >> i) & 1)
            if remainder >= divisor:
                remainder = remainder - divisor
                quotient = quotient | 1 << i
        return quotient
