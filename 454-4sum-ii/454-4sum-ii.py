class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        c = Counter(x+y for x in nums1 for y in nums2)
        return sum(c[-x-y] for x in nums3 for y in nums4)