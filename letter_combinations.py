from typing import List


# Heap's algorithm
# https://en.wikipedia.org/wiki/Heap%27s_algorithm
def perm(A: List[int]) -> List[List[int]]:
    output = []
    perm_helper(A, len(A), output)
    return output


def perm_helper(A: List[int], k: int, output: List[List[int]]) -> None:
    if k == 1:
        output.append(A.copy())
    else:
        # permutations with last element fixed
        perm_helper(A, k - 1, output)
        # permutations with last element swapped out
        for i in range(k - 1):
            if k % 2 == 0:  # k is even
                swap(A, i, k - 1)
            else:
                swap(A, 0, k - 1)
            perm_helper(A, k - 1, output)


def swap(A: List[int], i: int, j: int):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class LetterCombinations:
    table = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    @classmethod
    def solve(cls, digits: str) -> List[str]:
        if not digits:
            return []

        letters = []
        for d in digits:
            letters.append(cls.table[d])

        output = []
        cls.helper(letters, len(letters), 0, "", output)
        return output

    @classmethod
    def helper(cls, letters: List[str], n: int, ind: int, comb: str, output: List[str]):
        if ind > n - 1:
            output.append(comb)
            return

        for l in letters[ind]:
            comb += l
            cls.helper(letters, n, ind + 1, comb, output)
            comb = comb[:-1]
