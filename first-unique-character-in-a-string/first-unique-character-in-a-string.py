class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = [0] * 26
        # Get a count of all chars
        for ch in s:
            # ord() gets us the ascii code, and -97 will
            # allow us to use 0-25 indexing for the counts array.
            # ex) ord(a) == 97 ... ord(z) == 122
            #     97 - 97 = 0  ... 122 - 97 = 25
            counts[ord(ch)-97] += 1
        # Now go through the string and check if the char count == 1
        for i, ch in enumerate(s):
            if counts[ord(ch)-97] == 1:
                return i
        # If none are found
        return -1