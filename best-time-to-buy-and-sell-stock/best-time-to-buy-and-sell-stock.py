class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return max([s - b for s, b in zip(prices, accumulate(prices, min))]) if len(prices) else 0