class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid 
            else:
                l = mid
        return l if nums[l] >= target else l + 1