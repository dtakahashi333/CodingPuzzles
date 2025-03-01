from unittest import TestCase
from best_time_to_buy_and_sell_stock import BestTimeToBuyAndSellStock


class TestBestTimeToBuyAndSellStock(TestCase):

    def test_solve_by_brute_force1(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        self.assertEqual(expected, BestTimeToBuyAndSellStock.solveByBruteForce(prices))

    def test_solve_by_brute_force2(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        self.assertEqual(expected, BestTimeToBuyAndSellStock.solveByBruteForce(prices))

    def test_solve_by_optimal1(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        self.assertEqual(expected, BestTimeToBuyAndSellStock.solveByOptimal(prices))

    def test_solve_by_optimal2(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        self.assertEqual(expected, BestTimeToBuyAndSellStock.solveByOptimal(prices))
