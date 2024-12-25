# Best Time to Buy and Sell Stock
from typing import List


class Solution:
    def SellBuy(self, prices: List[int]) -> int:
        buy_cost = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_cost > p:
                buy_cost = p
            profit = max(profit, p-buy_cost)
        return profit

if __name__ == "__main__":
    solution = Solution()
    prices = [7,5,3,1,6,9]
    res = solution.SellBuy(prices)
    print(res)
