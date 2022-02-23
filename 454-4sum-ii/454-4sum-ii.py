class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        m = defaultdict(int)
        lists = [nums1, nums2, nums3, nums4]
        
        def nSumCount() -> int:
            addToHash(0,0)
            return countComplements(len(lists) // 2, 0)
        
        def addToHash(i: int, total: int) -> None:
            if i == len(lists) // 2:
                m[total] = m[total] + 1
            else:
                for a in lists[i]:
                    addToHash(i+1, total+a)
        
        def countComplements(i: int, complement: int) -> int:
            if i == len(lists):
                return m[complement]
            cnt = 0
            for a in lists[i]:
                cnt += countComplements(i+1, complement -a)
            return cnt
        
        return nSumCount()
            