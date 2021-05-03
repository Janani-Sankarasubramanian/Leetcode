import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for n in nums:
            if out:
                out.append(out[-1]*n)
            else:
                out.append(n)
        right = None
        i = len(nums)-1
        while i>=0:
            if right!=None:
                right = right*nums[i+1]
            else:
                right = 1
            if i-1>=0:
                out[i] = out[i-1]*right
            else:
                out[i] = right
            i = i-1
        return out