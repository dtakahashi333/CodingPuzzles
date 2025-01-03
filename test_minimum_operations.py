from unittest import TestCase
from minimum_operations import MinimumOperations


class TestMinimumOperations(TestCase):

    def test_solve(self):
        grid = [[3, 2], [1, 3], [3, 4], [0, 1]]
        expected = 15
        self.assertEqual(expected, MinimumOperations.solve(grid))
        grid = [[3, 2, 1], [2, 1, 0], [1, 2, 3]]
        expected = 12
        self.assertEqual(expected, MinimumOperations.solve(grid))
