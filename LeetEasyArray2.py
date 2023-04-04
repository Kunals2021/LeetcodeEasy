#You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#On each day, you may decide to buy and/or sell the stock. 
#You can only hold at most one share of the stock at any time. 
#However, you can buy it then immediately sell it on the same day.
#Find and return the maximum profit you can achieve
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0

        # iterate over the prices array
        for i in range(1, len(prices)):
            # check if the current price is higher than the previous price
            if prices[i] > prices[i-1]:
                # add the difference to the max_profit variable
                max_profit += prices[i] - prices[i-1]

        # return the maximum profit
        return max_profit
