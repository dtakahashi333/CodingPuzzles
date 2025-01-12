# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
class RomanToInt:

    @staticmethod
    def solve(s: str) -> int:
        hmap = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        n, i = len(s), 0
        num = 0
        while i < n:
            if s[i] == "I" and i + 1 < n and (s[i:i + 2] == "IV" or s[i:i + 2] == "IX"):
                # Look ahead one character to see if it is "IV" or "IX".
                num += hmap[s[i:i + 2]]
                i += 1
            elif s[i] == "X" and i + 1 < n and (s[i:i + 2] == "XL" or s[i:i + 2] == "XC"):
                # Look ahead one character to see if it is "XL" or "LC".
                num += hmap[s[i:i + 2]]
                i += 1
            elif s[i] == "C" and i + 1 < n and (s[i:i + 2] == "CD" or s[i:i + 2] == "CM"):
                # Look ahead one character to see if it is "CD" or "CM".
                num += hmap[s[i:i + 2]]
                i += 1
            else:
                num += hmap[s[i]]
            i += 1

        return num
