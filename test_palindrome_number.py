from unittest import TestCase
from palindrome_number import PalindromeNumber

class TestPalindromeNumber(TestCase):

    def test_solve(self):
        x = 121
        expected = True
        self.assertEqual(expected, PalindromeNumber.solve(x))
        x = -121
        expected = False
        self.assertEqual(expected, PalindromeNumber.solve(x))
        x = 10
        expected = False
        self.assertEqual(expected, PalindromeNumber.solve(x))
