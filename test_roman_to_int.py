from unittest import TestCase
from roman_to_int import RomanToInt


class TestRomanToInt(TestCase):

    def test_solve(self):
        s = "III"
        expected = 3
        self.assertEqual(expected, RomanToInt.solve(s))
        s = "LVIII"
        expected = 58
        self.assertEqual(expected, RomanToInt.solve(s))
        s = "MCMXCIV"
        expected = 1994
        self.assertEqual(expected, RomanToInt.solve(s))
