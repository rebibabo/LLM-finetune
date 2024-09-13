class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i, max = 0, 0
        while i <= max and i < len(nums):
            if nums[i] + i > max:
                max = nums[i] + i
                if max == len(nums) - 1:
                    break
            i += 1
        if max >= len(nums) - 1:
            return True
        else:
            return False