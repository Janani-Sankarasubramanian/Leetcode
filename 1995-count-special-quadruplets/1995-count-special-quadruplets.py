class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        n = len(nums)
        count = 0
        for a in range(n-1, -1, -1):
            for b in range(a-1, -1, -1):
                for c in range(b-1, -1, -1):
                    maybe_d = nums[a] + nums[b] + nums[c]
                    if maybe_d in seen:
                        count += seen[maybe_d]
            seen[nums[a]] += 1
        return count
