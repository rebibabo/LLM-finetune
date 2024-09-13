class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.find(candidates, target, ans, [], 0)
        return ans
    
    def find(self, candidates, target, ans, s, idx):
        if not target:
            ans.append(s[:])
            return
        if idx == len(candidates):
            return
        self.find(candidates, target, ans, s, idx + 1)
        if target - candidates[idx] >= 0:
            s.append(candidates[idx])
            self.find(candidates, target - candidates[idx], ans, s, idx)
            s.pop()