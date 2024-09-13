class Solution:
    
    def jump(self, nums: List[int]) -> int:
        steps = [0] * len(nums)
        i, max_jump = 0, 0
        while i <= max_jump and i < len(nums):
            if nums[i] + i > max_jump:
                for j in range(max_jump+1, min(len(nums), nums[i] + i + 1)):
                    steps[j] = steps[i] + 1
                max_jump = nums[i] + i
                if max_jump >= len(nums) - 1:
                    break
            i += 1
        return steps[-1]