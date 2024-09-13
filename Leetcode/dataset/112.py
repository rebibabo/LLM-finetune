class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        return self.find(root, targetSum, 0)

    def find(self, root, targetSum, currentSum):
        if not root:
            return False
        if currentSum + root.val == targetSum and not root.left and not root.right:
            return True
        return self.find(root.left, targetSum, currentSum + root.val) or self.find(root.right, targetSum, currentSum + root.val)