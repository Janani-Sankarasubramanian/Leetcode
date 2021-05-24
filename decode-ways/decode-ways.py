from functools import lru_cache
class Solution(object):
    
    def numDecodings(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """
        @lru_cache(maxsize=None)
        def recursiveWithMemo(index, s) -> int:
            # If you reach the end of the string
            # Return 1 for success.
            if index == len(s):
                return 1

            # If the string starts with a zero, it can't be decoded
            if s[index] == '0':
                return 0

            if index == len(s)-1:
                return 1
        
            answer = recursiveWithMemo(index + 1, s)
            if int(s[index : index + 2]) <= 26:
                answer += recursiveWithMemo(index + 2, s)

            return answer
        return recursiveWithMemo(0, s)