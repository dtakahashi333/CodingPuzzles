# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/editorial/
class LongestPalindrome:

    @staticmethod
    def solveByBruteForce(s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        palindrome = []
        for i in range(n):
            j = n - 1
            while i < j:
                if s[i] == s[j]:
                    # check if the substring is a palindrome.
                    head, tail = "", ""
                    k, l = i, j
                    while k < l:
                        if s[k] != s[l]:
                            break
                        head = head + s[k]
                        tail = s[k] + tail
                        k += 1
                        l -= 1
                    if k == l and s[k] == s[l]:
                        # palindrome
                        palindrome.append(head + s[k] + tail)
                        break
                    if k > l:
                        # palindrome
                        palindrome.append(head + tail)
                        break
                j -= 1
        # find a longest palindrome.
        longest = ""
        for pal in palindrome:
            if len(pal) > len(longest):
                longest = pal
        if longest == "":
            longest = "" + s[0]
        return longest

    @staticmethod
    def solveByTabulation(s: str) -> str:
        n = len(s)
        dp = []
        for _ in range(n):
            dp.append([False] * n)

        # Initialization
        pal = s[0]  # Any single character is a palindrome.
        for i in range(n):
            dp[i][i] = True

        for i in range(0, n - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])
            if dp[i][i + 1]:
                pal = s[i:i + 2]

        for dif in range(2, n):
            for i in range(0, n - dif):
                j = i + dif
                dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
                if dp[i][j]:
                    pal = s[i:j + 1]

        for i in range(n):
            for j in range(n):
                print(dp[i][j], end=" ")
            print()
        print()

        return pal

    # Wrong Answer!!!
    @staticmethod
    def solveByTabulationWrong(s: str) -> str:
        # Use table to figure out the palindrome.
        n = len(s)
        # Initialize the table.
        dp = []
        for _ in range(n + 1):
            dp.append([0] * (n + 1))

        max_len = 0
        max_i, max_j = 0, 0
        for i in range(n):
            j = 0
            for k in range(n - 1, -1, -1):
                if s[i] == s[k]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                    if dp[i + 1][j + 1] > max_len:
                        max_len = dp[i + 1][j + 1]
                        max_i, max_j = i + 1, j + 1
                j += 1

        for i in range(n + 1):
            for j in range(n + 1):
                print(dp[i][j], end=" ")
            print()
        print()

        pal = ""
        i, j = max_i, max_j
        while True:
            pal = s[i - 1] + pal
            if dp[i - 1][j - 1] == 0 or dp[i - 1][j - 1] >= dp[i][j]:
                break
            i, j = i - 1, j - 1

        return pal

    @staticmethod
    def solveByCenterExpansion(s: str) -> str:
        n = len(s)
        pal = s[0]  # Initialize the first character of the string as a palindrome.
        # A center is moving from left to right.
        for c in range(n):
            # Odd number of characters in the palindrome.
            # Distance from the center index.
            for d in range(1, n):
                i, j = c - d, c + d  # i is a left index and j is a right index.
                if i < 0 or j > n - 1:
                    # Move onto the next center index.
                    break
                if s[i] != s[j]:
                    break
                if j - i + 1 > len(pal):
                    pal = s[i:j + 1]  # Keep the largest palindrome.

        for c in range(n - 1):
            # Even number of characters in the palindrome.
            c1, c2 = c, c + 1
            if s[c1] == s[c2]:
                if len(pal) < 2:
                    pal = s[c1:c2 + 1]
                # Distance from the center index.
                for d in range(1, n):
                    i, j = c1 - d, c2 + d  # i is a left index and j is a right index.
                    if i < 0 or j > n - 1:
                        # Move onto the next center index.
                        break
                    if s[i] != s[j]:
                        break
                    if j - i + 1 > len(pal):
                        pal = s[i:j + 1]  # Keep the largest palindrome.

        return pal

    # The below code is from LeetCode for my reference.
    @staticmethod
    def solveByManchester(s: str) -> str:
        s_prime = "#" + "#".join(s) + "#"
        n = len(s_prime)
        palindrome_radii = [0] * n
        center = radius = 0

        for i in range(n):
            mirror = 2 * center - i

            if i < radius:
                palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])

            while (
                    i + 1 + palindrome_radii[i] < n
                    and i - 1 - palindrome_radii[i] >= 0
                    and s_prime[i + 1 + palindrome_radii[i]]
                    == s_prime[i - 1 - palindrome_radii[i]]
            ):
                palindrome_radii[i] += 1

            if i + palindrome_radii[i] > radius:
                center = i
                radius = i + palindrome_radii[i]

        max_length = max(palindrome_radii)
        center_index = palindrome_radii.index(max_length)
        start_index = (center_index - max_length) // 2
        longest_palindrome = s[start_index: start_index + max_length]

        return longest_palindrome
