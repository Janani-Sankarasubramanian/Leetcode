class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxi_width = 0
        maxi_height = 0
        verticalCuts = sorted(verticalCuts)
        horizontalCuts = sorted(horizontalCuts)
        maxi_height = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            maxi_height = max(maxi_height, horizontalCuts[i]-horizontalCuts[i-1])
        maxi_width = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            maxi_width = max(maxi_width, verticalCuts[i]-verticalCuts[i-1])
        return (maxi_height*maxi_width) % (10**9 + 7)