class Solution:
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.construct(nums)

    def construct(self, nums):
        if not nums:
            return
        mid = len(nums) // 2
        left = self.construct(nums[:mid])
        right = self.construct(nums[mid+1:])
        return TreeNode(nums[mid], left, right)