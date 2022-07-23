class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = l = 0
        for j, c in zip(range(len(s)),s):
            if c in s[i:j]:
                if l < len(s[i:j]):
                    l = len(s[i:j])
                i += s[i:j].index(c) + 1
        if l < len(s[i:j+1]):
            l = len(s[i:j+1])
        return l
    
