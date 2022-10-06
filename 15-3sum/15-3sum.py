class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        res = []
        nums.sort()
        if nums[0] > 0 or nums[-1] <0:
            return []
        
        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            L = i+1
            R = len(nums) - 1
            while L < R:
                sumNow = nums[L] + nums[R]
                if sumNow < target:
                    L+=1
                elif sumNow > target:
                    R-=1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    while (L<R and nums[R] == nums[R-1]): R-=1
                    L+=1
                    R-=1
        return res