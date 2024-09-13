class Solution:
    def buildTree(self, inorder, postorder):
        return self.construct(inorder, postorder)

    def construct(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        r_val = postorder[-1]
        root = TreeNode(r_val)
        i = inorder.index(r_val)
        left_inorder = inorder[:i]
        right_inorder = inorder[i+1:]
        left_postorder = postorder[0:i]
        right_postorder = postorder[i:-1]
        root.left = self.construct(left_inorder, left_postorder)
        root.right = self.construct(right_inorder, right_postorder)
        return root