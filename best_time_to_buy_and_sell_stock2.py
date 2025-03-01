from typing import List


# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150
class BestTimeToBuyAndSellStock2:

    @classmethod
    def solveByMemoization(cls, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        return cls.helperByMemoization(prices, n, 0, 1, dp)

    @classmethod
    def helperByMemoization(cls, prices: List[int], n: int, ind: int, canBuy: int, dp: List[List[int]]) -> int:
        if ind == n:  # The last price
            return 0

        # Memoization
        if dp[ind][canBuy] != -1:
            return dp[ind][canBuy]

        if canBuy:
            # Any stock is not purchased yet, a possible action is buy or not buy.
            dp[ind][canBuy] = max(
                -prices[ind] + cls.helperByMemoization(prices, n, ind + 1, 0, dp),  # Buy
                cls.helperByMemoization(prices, n, ind + 1, canBuy, dp)  # Not buy
            )
        else:
            # A stock is already purchased, a possible action is sell or not sell.
            dp[ind][canBuy] = max(
                prices[ind] + cls.helperByMemoization(prices, n, ind + 1, 1, dp),  # Sell
                cls.helperByMemoization(prices, n, ind + 1, canBuy, dp)  # Not sell
            )
        return dp[ind][canBuy]

    @classmethod
    def solveByTabulation(cls, prices: List[int]) -> int:
        n = len(prices)
        # Space complexity O(2n)
        dp = [[-1] * 2 for _ in range(n + 1)]
        # Initialization
        dp[n][0], dp[n][1] = 0, 0
        for i in range(n - 1, -1, -1):
            dp[i][1] = max(
                -prices[i] + dp[i + 1][0],  # Buy
                dp[i + 1][1]  # Not buy
            )
            dp[i][0] = max(
                prices[i] + dp[i + 1][1],  # Sell
                dp[i + 1][0]  # Not sell
            )
        return dp[0][1]

    @classmethod
    def solveByTabulationOptimal(cls, prices: List[int]) -> int:
        n = len(prices)
        # Space complexity O(4)
        cur_profit, next_profit = [-1] * 2, [-1] * 2
        # Initialization
        next_profit[0], next_profit[1] = 0, 0
        for i in range(n - 1, -1, -1):
            cur_profit[1] = max(
                -prices[i] + next_profit[0],  # Buy
                next_profit[1]  # Not buy
            )
            cur_profit[0] = max(
                prices[i] + next_profit[1],  # Sell
                next_profit[0]  # Not sell
            )
            next_profit = cur_profit
        return next_profit[1]
