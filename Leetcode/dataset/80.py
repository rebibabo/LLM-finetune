class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s, j, c = 0, 0, nums[0] 
        for i in range(len(nums)):
            if nums[i] == c:
                s += 1
                if s > 2:
                    continue
            else:
                s = 1
                c = nums[i]
            nums[j] = nums[i]
            j += 1
        return j