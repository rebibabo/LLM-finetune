class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        l = len(nums)
        for i in range(1, l):
            res[i] = res[i-1] * nums[i-1]
        suffix_prod = 1
        for i in range(l-2, -1, -1):
            suffix_prod *= nums[i+1]
            res[i] *= suffix_prod
        return res