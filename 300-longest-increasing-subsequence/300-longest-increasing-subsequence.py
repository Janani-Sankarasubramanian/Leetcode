class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [0] * len(nums)
        size = 0
        for x in nums:
            i,j= 0, size
            while i != j:
                m = (i+j) // 2
                if sub[m] < x:
                    i = m+1
                else:
                    j=m
            sub[i] = x
            size = max(i+1, size)
        return size

