from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={}
        dic[0]=1
        summ=count=0
        for i in nums:
            summ+=i
            if summ-k in dic:
                count+=dic[summ-k]
            if summ not in dic:
                dic[summ]=1
            else:
                dic[summ]+=1   
        return count

