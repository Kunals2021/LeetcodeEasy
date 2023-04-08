# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a 
# different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize minimum price to a large value and maximum profit to 0
        min_price = float('inf')
        max_profit = 0
        
        # Iterate through the prices array
        for price in prices:
            # If the current price is lower than the minimum price, update the minimum price
            if price < min_price:
                min_price = price
            # Otherwise, calculate the profit we would make if we sold at the current price
            else:
                profit = price - min_price
                # If the profit is greater than the current maximum profit, update the maximum profit
                if profit > max_profit:
                    max_profit = profit
        
        # Return the maximum profit
        return max_profit

# We first initialize the minimum price to a large value and the maximum profit to 0. 
# Then, we iterate through the prices array and for each price, we check if it is lower than
#  the current minimum price. If it is, we update the minimum price to the current price. 
# If it is not, we calculate the profit we would make if we sold at the current price 
# (i.e., the difference between the current price and the minimum price). If the profit is greater 
# than the current maximum profit, we update the maximum profit.
# At the end of the loop, we return the maximum profit. This approach works because we are essentially 
# trying to find the maximum difference between any two prices in the prices array, where the
#  second price is greater than the first price. By keeping track of the minimum price seen so far, 
# we can calculate the profit we would make if we sold at each subsequent price and update the 
# maximum profit accordingly.
