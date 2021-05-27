class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        h = max(map(lambda a: a[0] - a[1], zip(horizontalCuts + [h], [0] + horizontalCuts)))
        w = max(map(lambda a: a[0] - a[1], zip(verticalCuts + [w], [0] + verticalCuts)))
        return h * w % 1000000007