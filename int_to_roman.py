# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/description/
class IntToRoman:

    @staticmethod
    def solve(num: int) -> str:
        lst = []
        while num > 0:
            d = num % 10
            num //= 10
            lst.append(d)

        sym = ""
        for i in range(len(lst)):
            d = lst[i]
            if i == 0:
                if d == 4:
                    tmp = "IV"
                elif d == 9:
                    tmp = "IX"
                else:
                    if d >= 5:
                        tmp = "V"
                        d -= 5
                    else:
                        tmp = ""
                    for _ in range(d):
                        tmp += "I"
            elif i == 1:
                if d == 4:
                    tmp = "XL"
                elif d == 9:
                    tmp = "XC"
                else:
                    if d >= 5:
                        tmp = "L"
                        d -= 5
                    else:
                        tmp = ""
                    for _ in range(d):
                        tmp += "X"
            elif i == 2:
                if d == 4:
                    tmp = "CD"
                elif d == 9:
                    tmp = "CM"
                else:
                    if d >= 5:
                        tmp = "D"
                        d -= 5
                    else:
                        tmp = ""
                    for _ in range(d):
                        tmp += "C"
            else:
                tmp = ""
                for _ in range(d):
                    tmp += "M"
            sym = tmp + sym
        return sym
