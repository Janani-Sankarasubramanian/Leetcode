class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxi_width,maxi_height  = 0,0
        verticalCuts.sort()
        horizontalCuts.sort()
        if horizontalCuts[0] <= h - horizontalCuts[-1]:
            maxi_height = h - horizontalCuts[-1]
        else:
            maxi_height = horizontalCuts[0] 

        for i in range(1, len(horizontalCuts)):
            if maxi_height <= horizontalCuts[i]-horizontalCuts[i-1]:
                maxi_height = horizontalCuts[i]-horizontalCuts[i-1]
                
        if verticalCuts[0] <= w - verticalCuts[-1]:
            maxi_width = w - verticalCuts[-1]
        else:
            maxi_width = verticalCuts[0]
            
        for i in range(1, len(verticalCuts)):
            if maxi_width <= verticalCuts[i]-verticalCuts[i-1]:
                maxi_width = verticalCuts[i]-verticalCuts[i-1]
                
        return (maxi_height*maxi_width) % (10**9 + 7)