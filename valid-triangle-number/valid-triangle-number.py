class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def binarySearch(nums, l, r, x):
            while r>=l and r< len(nums):
                mid = (l+r)//2
                if nums[mid] >= x:
                    r = mid-1
                else:
                    l = mid+1
            return l

        count = 0
        nums.sort()
        for i in range(len(nums) -2):
            k = i+2
            if nums[i] != 0:
                for j in range(i+1, len(nums)-1):
                    k = binarySearch(nums, k, len(nums) - 1, nums[i]+nums[j])
                    count += k-j-1
        return count