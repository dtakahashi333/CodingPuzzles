# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/
class ZigzagConversion:

    @staticmethod
    def solve(s: str, numRows: int) -> str:
        n = len(s)
        zigzag_list = []
        i = 0
        while i < n:
            inner = [""] * numRows
            for j in range(numRows):
                if i > n - 1:
                    break
                inner[j] = s[i]
                i += 1

            zigzag_list.append(inner)

            for j in range(numRows - 2, 0, -1):
                if i > n - 1:
                    break
                inner = [""] * numRows
                inner[j] = s[i]
                zigzag_list.append(inner)
                i += 1

        result = ""
        for j in range(numRows):
            for i in range(len(zigzag_list)):
                result += zigzag_list[i][j]
        return result
