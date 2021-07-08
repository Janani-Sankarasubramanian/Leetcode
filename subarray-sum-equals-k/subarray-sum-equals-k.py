from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, sum = 0, 0
        running_sum = defaultdict(int)
        running_sum[0] = 1
        
        for n in nums:
            sum += n
            count += running_sum[sum-k]
            running_sum[sum] += 1

        return count

