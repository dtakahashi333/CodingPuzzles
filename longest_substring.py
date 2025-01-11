# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class LongestSubstring:

    @staticmethod
    def solve_by_brute_force(s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            chrs = [0] * 128
            chrs[ord(s[i])] = 1
            count = 1
            for j in range(i + 1, n, 1):
                pos = ord(s[j])
                if chrs[pos] == 0:
                    count += 1
                    chrs[pos] = 1
                else:
                    break
                j += 1
            if count > max_len:
                max_len = count
        return max_len

    # solution by ChatGPT.
    @staticmethod
    def solve(s: str) -> int:
        # Initialize a set to store the unique characters in the current window
        char_set = set()
        start = 0  # The left end of the window
        max_length = 0  # The length of the longest substring found

        # Loop through the string with the `end` pointer
        for end in range(len(s)):
            # If the character is in the set, move the `start` pointer to remove duplicates
            while s[end] in char_set:
                char_set.remove(s[start])  # Remove character at the start pointer
                start += 1  # Move start pointer right to shrink the window

            # Add the current character to the set
            char_set.add(s[end])

            # Update the max_length with the size of the current window
            max_length = max(max_length, end - start + 1)

        return max_length
