class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        freq = {} #Map
        left_1 = 0 #First left pointer
        left_2 = 0 #second left pointer
        res = 0 #result
        for i, x in enumerate(A):
            freq[x] = freq.get(x, 0) + 1 #update the map with the count
            if len(freq) == K + 1:
                # remove the distinct from left_2, move left_2, left_1
                del freq[A[left_2]]
                left_2 += 1
                left_1 = left_2
            if len(freq) == K:
                # update left_2 and res (Notice: K >= 1)
                while freq[A[left_2]] > 1:
                    freq[A[left_2]] -= 1
                    left_2 += 1
                res += left_2 - left_1 +1
        return res