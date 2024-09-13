class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        self.nums = nums
        while l <= r:
            mid = (l + r) // 2
            if self.get(mid-1) < self.get(mid) > self.get(mid+1):
                return mid
            if self.get(mid - 1) > self.get(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

    def get(self, i):
        if i < 0 or i >= len(self.nums):
            return float("-inf")
        return self.nums[i]