class Solution(object):
    
    def numDecodings(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0" or s is None or len(s)==0:
            return 0
    
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1 if s[0]!='0' else 0
        for i in range(2, len(s)+1):
            first = int(s[i-1:i])
            second = int(s[i-2:i])
            if first>=1 and first<=9:
                dp[i] += dp[i-1]
            
            if second>=10 and second<=26:
                dp[i] += dp[i-2]
                
        return dp[len(s)]