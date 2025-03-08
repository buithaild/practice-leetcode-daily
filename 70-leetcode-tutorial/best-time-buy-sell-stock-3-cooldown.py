# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
#
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
from typing import List


# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # State: Buying or Selling
        # If buy -> i+1
        # If sell -> i + 2

        dp = {} # key=(i,buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)

            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)

            else:
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max((sell, cooldown))

            return dp[(i, buying)]
        return dfs(0, True)

if __name__ == "__main__":
    solution = Solution()
    s = Solution()
    prices = [1,2,3,0,2]
    res = s.maxProfit(prices)
    print(res)


