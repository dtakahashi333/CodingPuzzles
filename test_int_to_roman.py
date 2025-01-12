from unittest import TestCase
from int_to_roman import IntToRoman


class TestIntToRoman(TestCase):

    def test_solve(self):
        num = 3749
        expected = "MMMDCCXLIX"
        self.assertEqual(expected, IntToRoman.solve(num))
        num = 58
        expected = "LVIII"
        self.assertEqual(expected, IntToRoman.solve(num))
        num = 1994
        expected = "MCMXCIV"
        self.assertEqual(expected, IntToRoman.solve(num))
