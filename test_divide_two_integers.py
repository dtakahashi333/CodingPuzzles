from unittest import TestCase
from divide_two_integers import DivideTwoIntegers
import math


class TestDivideTwoIntegers(TestCase):

    def test_solve_1(self):
        dividend = 10
        divisor = 3
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))

    def test_solve_2(self):
        dividend = 7
        divisor = -3
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))

    def test_solve_3(self):
        dividend = 1
        divisor = 1
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))

    def test_solve_4(self):
        dividend = -2147483648
        divisor = -1
        expected = 2147483647
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))

    def test_solve_5(self):
        dividend = 2147483647
        divisor = 2
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))

    def test_solve_6(self):
        dividend = -2147483648
        divisor = 1
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))

    def test_solve_7(self):
        dividend = -2147483648
        divisor = 2
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve(dividend, divisor))

    def test_solve2_1(self):
        dividend = 10
        divisor = 3
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve2(dividend, divisor))

    def test_solve2_2(self):
        dividend = 7
        divisor = -3
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve2(dividend, divisor))

    def test_solve2_3(self):
        dividend = 1
        divisor = 1
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve2(dividend, divisor))

    def test_solve2_4(self):
        dividend = -2147483648
        divisor = -1
        expected = 2147483647
        self.assertEquals(expected, DivideTwoIntegers.solve2(dividend, divisor))

    def test_solve2_5(self):
        dividend = 2147483647
        divisor = 2
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve2(dividend, divisor))

    def test_solve2_6(self):
        dividend = -2147483648
        divisor = 1
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve2(dividend, divisor))

    def test_solve2_7(self):
        dividend = -2147483648
        divisor = 2
        expected = math.trunc(dividend / divisor)
        self.assertEquals(expected, DivideTwoIntegers.solve2(dividend, divisor))
