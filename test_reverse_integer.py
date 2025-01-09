from unittest import TestCase
from reverse_integer import ReverseInteger


class TestReverseInteger(TestCase):

    def test_reverse_integer(self):
        x = 123
        expected = 321
        self.assertEqual(expected, ReverseInteger.reverse_integer(x))
        x = -123
        expected = -321
        self.assertEqual(expected, ReverseInteger.reverse_integer(x))
        x = 120
        expected = 21
        self.assertEqual(expected, ReverseInteger.reverse_integer(x))
