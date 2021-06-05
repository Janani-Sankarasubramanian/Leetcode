class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return s

        ans = ""
        length = len(s)
        dp = [False for i in range(length)]
        for j in range(length):
            for i in range(j+1):
                if i == j:
                    dp[i] = True
                elif j == i+1:
                    dp[i] = (s[i]==s[j])
                else:
                    dp[i] = (dp[i+1] and s[i]==s[j])

                if dp[i] and j-i+1 > len(ans):
                    ans = s[i:j+1]

        return ans