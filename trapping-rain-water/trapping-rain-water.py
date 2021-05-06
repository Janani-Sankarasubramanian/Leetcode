class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0]*len(height)
        rightMax = [0]*len(height)
        result = [0]*len(height)
        maxItem=0
        for i in range(len(height)):
            maxItem = max(maxItem, height[i])
            leftMax[i] = maxItem
        maxItem=0
        for i in reversed(range(len(height))):
            maxItem = max(maxItem, height[i])
            rightMax[i] = maxItem
        for i in range(len(height)):
            result[i] = min(leftMax[i], rightMax[i]) - height[i]
        return sum(result)