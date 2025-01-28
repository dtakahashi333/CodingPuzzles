from unittest import TestCase
from divide_two_integers import DivideTwoIntegers
import math


class TestDivideTwoIntegers(TestCase):

    def test_solve1(self):
        dividend = 10
        divisor = 3
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))

    def test_solve2(self):
        dividend = 7
        divisor = -3
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))

    def test_solve3(self):
        dividend = 1
        divisor = 1
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))

    def test_solve4(self):
        dividend = -2147483648
        divisor = -1
        expected = 2147483647
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))

    def test_solve5(self):
        dividend = 2147483647
        divisor = 2
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))

    def test_solve6(self):
        dividend = -2147483648
        divisor = 1
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))

    def test_solve7(self):
        dividend = -2147483648
        divisor = 2
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))
