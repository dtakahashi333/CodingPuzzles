from unittest import TestCase
from string_to_integer import StringToInteger

class TestStringToInteger(TestCase):

    def test_solve(self):
        self.assertEqual(42, StringToInteger.solve("42"))
        self.assertEqual(-42, StringToInteger.solve("-042"))
        self.assertEqual(1337, StringToInteger.solve("1337c0d3"))
        self.assertEqual(0, StringToInteger.solve("0-1"))
        self.assertEqual(0, StringToInteger.solve("words and 987"))
