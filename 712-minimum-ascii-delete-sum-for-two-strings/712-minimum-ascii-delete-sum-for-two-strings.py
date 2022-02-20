class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[-1 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        
        def dead_end_sum(s, i):
            sum = 0
            while i < len(s):
                sum += ord(s[i])
                i += 1
            return sum
        
        def sub(a, b, i, j):
            n = len(a)
            m = len(b)
            if i ==n or j ==m:
                if i ==n and j ==m: return 0
                return dead_end_sum(b,j) if i==n else dead_end_sum(a,i)
            
            if dp[i][j] !=-1: return dp[i][j]
            if a[i] == b[j]:
                sum = sub(a,b,i+1,j+1)
            else:
                sum = min(sub(a,b,i+1,j) + ord(a[i]), sub(a,b,i,j+1) + ord(b[j]))
            dp[i][j] = sum
            return sum
        
        return sub(s1,s2,0,0)
        return 0    