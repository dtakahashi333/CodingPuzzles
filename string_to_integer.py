# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/description/

class StringToInteger:

    @staticmethod
    def solve(s: str) -> int:
        sign = None
        num_str = ""
        for c in s:
            if sign is not None or len(num_str) > 0: # Started getting an integer.
                if ord(c) < 48 or ord(c) > 57:
                    break
                else:
                    num_str += c
            elif c == " ":
                continue
            elif c == "-":
                sign = -1
            elif c == "+":
                sign = 1
            elif 48 <= ord(c) <= 57:
                if sign is None:
                    sign = 1
                num_str += c
            else:
                break
        if num_str == "":
            return 0
        num = 0
        for i in range(len(num_str)):
            num = num * 10 + int(num_str[i])
        num = sign * num
        if num < -pow(2, 31):
            return -pow(2, 31)
        if num > pow(2, 31) - 1:
            return pow(2, 31) - 1
        else:
            return num
