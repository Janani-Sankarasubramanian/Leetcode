class Solution:
    
    def find(self, parent, i):
        if parent[i] == -1:
            return i 
        return self.find(parent, parent[i])
    
    def union(self, parent, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if xroot != yroot:
            parent[xroot] = yroot
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        M_len = len(isConnected)
        parent = [-1]*M_len
        for i in range(M_len):
            for j in range(M_len):
                if isConnected[i][j] == 1 and i!=j:
                    self.union(parent, i, j)
        count = 0
        for i in range(M_len):
            if parent[i] == -1:
                count += 1
        return count
                    