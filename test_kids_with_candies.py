from unittest import TestCase
from kids_with_candies import KidsWithCandies


class TestKidsWithCandies(TestCase):

    def test_solve(self):
        candies = [2, 3, 5, 1, 3]
        extraCandies = 3
        expected = [True, True, True, False, True]
        self.assertListEqual(expected, KidsWithCandies.solve(candies, extraCandies))
        candies = [4, 2, 1, 1, 2]
        extraCandies = 1
        expected = [True, False, False, False, False]
        self.assertListEqual(expected, KidsWithCandies.solve(candies, extraCandies))
        candies = [12, 1, 12]
        extraCandies = 10
        expected = [True, False, True]
        self.assertListEqual(expected, KidsWithCandies.solve(candies, extraCandies))
