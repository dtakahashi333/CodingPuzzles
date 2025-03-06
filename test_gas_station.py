from unittest import TestCase
from gas_station import GasStation


class TestGasStation(TestCase):

    def test_solveByBruteForce1(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        expected = 3
        self.assertEqual(expected, GasStation.solveByBruteForce(gas, cost))

    def test_solveByBruteForce2(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        expected = -1
        self.assertEqual(expected, GasStation.solveByBruteForce(gas, cost))

    def test_solveByBruteForce3(self):
        gas = [3, 1, 1]
        cost = [1, 2, 2]
        expected = 0
        self.assertEqual(expected, GasStation.solveByBruteForce(gas, cost))

    def test_solveByBruteForce4(self):
        gas = [5, 8, 2, 8]
        cost = [6, 5, 6, 6]
        expected = 3
        self.assertEqual(expected, GasStation.solveByBruteForce(gas, cost))

    def test_solve1(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        expected = 3
        self.assertEqual(expected, GasStation.solve(gas, cost))

    def test_solve2(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        expected = -1
        self.assertEqual(expected, GasStation.solve(gas, cost))

    def test_solve3(self):
        gas = [3, 1, 1]
        cost = [1, 2, 2]
        expected = 0
        self.assertEqual(expected, GasStation.solve(gas, cost))

    def test_solve4(self):
        gas = [5, 8, 2, 8]
        cost = [6, 5, 6, 6]
        expected = 3
        self.assertEqual(expected, GasStation.solve(gas, cost))
