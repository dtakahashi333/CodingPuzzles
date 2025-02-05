# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/
# https://en.wikipedia.org/wiki/Division_algorithm
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

    @classmethod
    def solve2(cls, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        sign = 1
        if dividend < 0:
            sign = ~sign + 1
            dividend = ~dividend + 1
        if divisor < 0:
            sign = ~sign + 1
            divisor = ~divisor + 1
        quotient = cls.long_division2(dividend, divisor)
        if sign < 0:
            return ~quotient + 1  # To make the value negative
        else:
            return min(quotient, 2 ** 31 - 1)  # 2147483647 (32-bit integer-maximum)

    @classmethod
    def long_division2(cls, dividend: int, divisor: int) -> int:
        # Find out the most significant place value.
        place_value = 0
        m = dividend
        while m > 0:
            m = m // 10
            place_value = place_value + 1

        m = dividend
        quotient = 0
        remainder = 0
        for i in range(place_value - 1, -1, -1):
            quotient *= 10
            remainder *= 10
            remainder += (m // int(pow(10, i)))
            m = m % int(pow(10, i))
            if remainder >= divisor:
                while remainder >= divisor:
                    remainder -= divisor
                    quotient += 1
        return quotient
