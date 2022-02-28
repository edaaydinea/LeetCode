class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, low = 0, float('inf')

        for price in prices:
            if price - low > profit:
                profit = price - low
            if price < low:
                low = price

        return profit
