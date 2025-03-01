from typing import List
import sys

# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
# https://takeuforward.org/data-structure/stock-buy-and-sell/
# https://www.youtube.com/watch?v=eMSfBgbiEjk&t=200s
class BestTimeToBuyAndSellStock:

    @classmethod
    def solveByBruteForce(cls, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        # O(n^2)
        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

    @classmethod
    def solveByOptimal(cls, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        max_profit = 0
        # O(n)
        for i in range(1, n):
            cur_price = prices[i]
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, cur_price)
        return max_profit
