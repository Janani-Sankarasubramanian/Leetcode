class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        #dp array to store the state of transition
        dp = [[False]*length for _ in range(length)]
        ans = ""
        
        #if there is only one character, it is a palindrome
        for i in range(length):
            dp[i][i] = True
            ans = s[i]


        for start in range(length-1,-1,-1):
            for end in range(start+1, length):
                if s[start] == s[end]:
                    #if there are two or more characters, populate the dp array from the end. 
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if len(ans) < end-start +1:
                            ans = s[start:end+1]
        
        return ans