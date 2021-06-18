class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bs(start, tar):
            l, r = start, len(numbers)-1
            while l < r:
                m = l + ((r-l)>>1)
                if numbers[m]==tar:
                    return m
                elif numbers[m] > tar:
                    r = m-1
                else:
                    l = m+1
            return l if numbers[l]==tar else False
                           
        for i, n in enumerate(numbers):
            search = target-n
            idx = bs(i+1, search)
            if idx:
                return [i+1, idx+1]