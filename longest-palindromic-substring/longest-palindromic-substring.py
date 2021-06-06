class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length<2:
            return s

        length = 2*length + 1
        L = [0]*length
        L[0] = 0
        L[1] = 1
        C = 1 #center position
        R = 2 # center right position
        i = 0 #current right position
        iMirror = 0 #current left position
        maxLPSLength = 0
        maxLPSCenterPosition = 0
        start = -1
        end = -1
        diff = -1
        for i in range(2, length):
            #To get the center left position for the current right position
            iMirror = 2*C-i
            L[i] = 0
            diff = R- i
            # If currentRightPosition i is within centerRightPosition R
            if diff>0:
                L[i] = min(L[iMirror], diff)

            try:
        # Attempt to expand palindrome centered at currentRightPosition i
        # Here for odd positions, we compare characters and
        # if match then increment LPS Length by ONE
        # If even position, we just increment LPS by ONE without
        # any character comparison
                while ((i+L[i]) <length and (i-L[i])>0) and \
                    (((i+L[i]+1)%2 ==0) or \
                    (s[(i+L[i]+1)//2] == s[(i-L[i]-1)//2])):
                    L[i]+=1
            except Exception as e:
                pass

            if L[i] > maxLPSLength: # Track maxLPSLength 
                maxLPSLength = L[i]
                maxLPSCenterPosition = i

    # If palindrome centered at currentRightPosition i 
    # expand beyond centerRightPosition R, 
    # adjust centerPosition C based on expanded palindrome. 
            if i + L[i] > R:
                C = i
                R = i + L[i]

        start = (maxLPSCenterPosition - maxLPSLength)//2
        end = start + maxLPSLength - 1
        return s[start:end+1]
