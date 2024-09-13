class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l, r = -1, len(nums) - 1
        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid
        lfind = r if nums[r] == target else -1
        l, r = 0, len(nums)
        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        rfind = l if nums[l] == target else -1
        return [lfind, rfind]