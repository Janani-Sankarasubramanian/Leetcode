class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        inc = [float('inf')] * 2
        for x in nums:
            i = bisect_left(inc, x)
            if i >= 2:
                return True
            inc[i] = x
        return False
