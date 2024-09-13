class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        d = nums
        d[1] = max(d[1], d[0])
        for i in range(2, len(nums)):
            d[i] = max(d[i-2] + nums[i], nums[i-1])
        return d[-1]