# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        profit = 0
        min = max(prices) + 1
        
        for num in prices:
            if num < min:
                min = num
            else:
                profit = max(profit, num - min)
                
        return profit

# Runtime: 72 ms, faster than 15.35% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 13.7 MB, less than 98.85% of Python3 online submissions for Best Time to Buy and Sell Stock.

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        buy = 0
        sell = max(prices)
        
        for i in range(0, len(prices)):
            if prices[i] < sell:
                sell = prices[i]
            else:
                buy = max(buy, prices[i] - sell)
                
        return buy

# Runtime: 64 ms, faster than 57.51% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 13.9 MB, less than 75.86% of Python3 online submissions for Best Time to Buy and Sell Stock.