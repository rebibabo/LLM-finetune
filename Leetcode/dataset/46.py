class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.combine(nums, ans, [])
        return ans

    def combine(self, nums, ans, s):
        if not nums:
            ans.append(s[:])
            return
        for i, n in enumerate(nums):
            s.append(n)
            self.combine(nums[:i]+nums[i+1:], ans, s)
            s.pop()