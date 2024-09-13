class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = {}
        self.construct(equations, values)
        ans = []
        for q in queries:
            a, b = q
            if a not in self.graph or b not in self.graph:
                ans.append(-1)
            else:
                ans.append(self.dfs(a, b, set()))
        return ans

    def construct(self, equations, values): 
        for q, v in zip(equations, values):
            a, b = q
            self.graph.setdefault(a, [])
            self.graph[a].append((b, v))
            self.graph.setdefault(b, [])
            self.graph[b].append((a, 1/v))

    def dfs(self, a, b, visited):
        if a == b:  
            return 1
        visited.add(a)
        for c, v in self.graph[a]:
            if c not in visited:    
                t = self.dfs(c, b, visited) 
                if t != -1:     
                    return t * v
        return -1