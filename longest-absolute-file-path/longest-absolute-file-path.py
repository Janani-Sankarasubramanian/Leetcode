class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input = input.split("\n")
        st = [0]
        maxPath = 0
        for line in input:
            i = 0
            while i < len(line) and line[i] == "\t":i+=1
            while i+1 < len(st): st.pop()
            if "." in line:
                maxPath = max(st[-1]+len(line[i:]), maxPath)
            else:
                st.append(st[-1]+len(line[i:])+1)
        return maxPath