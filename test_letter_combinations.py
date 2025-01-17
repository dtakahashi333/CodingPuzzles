from unittest import TestCase
from letter_combinations import LetterCombinations, perm


class Test(TestCase):

    def test_permutations(self):
        A = [1, 2, 3]
        expected = [[1, 2, 3], [2, 1, 3], [3, 1, 2], [1, 3, 2], [2, 3, 1], [3, 2, 1]]
        self.assertListEqual(expected, perm([1, 2, 3]))


class TestLetterCombinations(TestCase):

    def test_solve(self):
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertCountEqual(expected, LetterCombinations.solve(digits))
        digits = ""
        expected = []
        self.assertCountEqual(expected, LetterCombinations.solve(digits))
        digits = "2"
        expected = ["a", "b", "c"]
        self.assertCountEqual(expected, LetterCombinations.solve(digits))
