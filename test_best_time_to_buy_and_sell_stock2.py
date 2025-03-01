from unittest import TestCase
from best_time_to_buy_and_sell_stock2 import BestTimeToBuyAndSellStock2


class TestBestTimeToBuyAndSellStock2(TestCase):

    def test_solveByMemoization1(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 7
        self.assertEqual(expected, BestTimeToBuyAndSellStock2.solveByMemoization(prices))

    def test_solveByMemoization2(self):
        prices = [1, 2, 3, 4, 5]
        expected = 4
        self.assertEqual(expected, BestTimeToBuyAndSellStock2.solveByMemoization(prices))

    def test_solveByMemoization3(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        self.assertEqual(expected, BestTimeToBuyAndSellStock2.solveByMemoization(prices))

    def test_solveByTabulation1(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 7
        self.assertEqual(expected, BestTimeToBuyAndSellStock2.solveByTabulation(prices))

    def test_solveByTabulation2(self):
        prices = [1, 2, 3, 4, 5]
        expected = 4
        self.assertEqual(expected, BestTimeToBuyAndSellStock2.solveByTabulation(prices))

    def test_solveByTabulation3(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        self.assertEqual(expected, BestTimeToBuyAndSellStock2.solveByTabulation(prices))

    def test_solveByTabulationOptimal1(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 7
        self.assertEqual(expected, BestTimeToBuyAndSellStock2.solveByTabulationOptimal(prices))

    def test_solveByTabulationOptimal2(self):
        prices = [1, 2, 3, 4, 5]
        expected = 4
        self.assertEqual(expected, BestTimeToBuyAndSellStock2.solveByTabulationOptimal(prices))

    def test_solveByTabulationOptimal3(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        self.assertEqual(expected, BestTimeToBuyAndSellStock2.solveByTabulationOptimal(prices))
