class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [1]
        for _ in range(n-1):
            i = ans[-1] 
            if 10*i <= n: 
                ans.append(10*i) 
            else:
                while i+1 > n or (i+1) % 10 == 0: 
                    i //= 10
                ans.append(i+1) 
        return ans