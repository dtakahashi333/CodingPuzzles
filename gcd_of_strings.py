# 1071. Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
class GcdOfStrings:

    @staticmethod
    def solve(str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        # n is longer. m is shorter.
        if n < m:
            temp = n
            n = m
            m = temp
        # calculate all common divisors.
        n_div = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                n_div.append(i)
                another = n // i
                if another != i:
                    n_div.append(another)
            i += 1
        m_div = []
        i = 1
        while i * i <= m:
            if m % i == 0:
                m_div.append(i)
                another = m // i
                if another != i:
                    m_div.append(another)
            i += 1
        common_divisors = sorted([i for i in n_div if i in m_div], reverse=True)

        for d in common_divisors:
            divisor = str1[:d]
            match = True
            for i in range(0, len(str1) - d + 1, d):
                if str1[i:i + d] != divisor:
                    match = False
                    break
            if match:
                for i in range(0, len(str2) - d + 1, d):
                    if str2[i:i + d] != divisor:
                        match = False
                        break
                if match:
                    return divisor
        return ""
