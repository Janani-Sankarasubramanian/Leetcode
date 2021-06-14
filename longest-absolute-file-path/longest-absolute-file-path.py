class Solution:
    def lengthLongestPath(self, input: str) -> int:
        if input==None and len(input)<1:
            return 0
        tabs = 0
        lines = input.split("\n")
        stack = []
        maxLen = 0
        curLen = 0
        for l in lines:
            l = l.split("\t")
            lTabs = len(l)
            while(tabs>=lTabs):
                item = stack.pop()
                if "." in item:
                    if maxLen<curLen + len(stack):
                        maxLen = curLen+len(stack)
                curLen -= len(item)
                tabs -= 1

            curLen += len(l[-1])
            stack.append(l[-1])
            tabs +=1

        if "." in stack[-1]:
            if maxLen<curLen + len(stack)-1:
                maxLen = curLen+len(stack)-1
            
        return maxLen