class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1)
        def recursive_climb(i, n, memo):
            
            if i > n:
                return 0 
            
            if i == n:
                return 1
            
            if memo[i] > 0:
                return memo[i]
            
            memo[i] = recursive_climb(i+1, n, memo) + recursive_climb(i+2, n, memo)
            return memo[i]
        
        return recursive_climb(0, n, memo)