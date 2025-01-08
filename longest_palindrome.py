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
