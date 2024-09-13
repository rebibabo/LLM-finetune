class Solution:
    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j, sum, min_l = 0, 0, 0, 10e5
        while j < len(nums):
            while j < len(nums) and sum < target:   
                sum += nums[j]
                j += 1 
            while i < len(nums) and sum >= target:
                if j - i < min_l:
                    min_l = j - i
                sum -= nums[i]
                i += 1
        if min_l == 10e5:
            return 0
        return min_l