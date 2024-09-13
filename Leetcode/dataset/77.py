class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n, self.k = n, k
        com = []
        for i in range(1, self.n-self.k+2):
            self.find(com, [i])     
        return com

    def find(self, com, s):
        if len(s) == self.k:    
            com.append(s[:])
            return
        for i in range(s[-1]+1, self.n+1):
            s.append(i)     
            self.find(com, s)   
            s.pop()