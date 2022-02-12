class Solution:
    def lcs(self, s1, s2, m, n, memo):
        if m ==0 or n==0:
            return 0 
        if memo[m][n] >0 :
            return memo[m][n]
        if s1[m-1] == s2[n-1]:
            memo[m][n] = 1 + self.lcs(s1, s2, m-1, n-1, memo)
        else:
            memo[m][n] = max(self.lcs(s1, s2, m, n-1, memo), self.lcs(s1,s2, m-1,n, memo))
        return memo[m][n]
        
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        return len(word1) + len(word2) - 2*self.lcs(word1, word2, len(word1), len(word2), memo)
    

        