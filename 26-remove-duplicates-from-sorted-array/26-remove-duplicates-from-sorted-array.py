class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_idx = 0
        right_idx = 1
        
        if nums is None:
            return 0
        
          
        while right_idx < len(nums):
            if nums[insert_idx] != nums[right_idx]:
                insert_idx +=1
                nums[insert_idx] = nums[right_idx]
            right_idx += 1
            
        return insert_idx + 1