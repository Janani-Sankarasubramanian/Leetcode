class Solution:
    def firstUniqChar(self, s: str) -> int:
        length = len(s)
        for i in range(length):
            pivot = s[i]
            if pivot in s[:i] or pivot in s[i+1:]:
                continue
            return i
        return -1