class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            #Create a dictionary - which will store target - nums[index] as a key and the index as its value
            #Traverse the nums list and return the index of the target - nums[index]
            
            out = []
            store_target = {}
            for i in range(len(nums)):
                store_target[target - nums[i]] = i
            
            for i in range(len(nums)):
                if nums[i] in store_target:
                    if i != store_target[nums[i]]:
                        out.append(i)
                        out.append(store_target[nums[i]])
                        return out
            