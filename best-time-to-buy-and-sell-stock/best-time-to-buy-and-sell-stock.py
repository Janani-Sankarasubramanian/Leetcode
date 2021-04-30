class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ending_here, max_so_far = 0, 0
        for prev, curr in zip(prices, prices[1:]):
            max_ending_here = max(max_ending_here + curr - prev, 0)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far