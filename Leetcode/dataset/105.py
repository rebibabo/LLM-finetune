class Solution:
    def buildTree(self, preorder, inorder):
        return self.construct(preorder, inorder)

    def construct(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        r_val = preorder[0]
        root = TreeNode(r_val)
        i = inorder.index(r_val)
        left_inorder = inorder[:i]
        right_inorder = inorder[i+1:]
        left_preorder = preorder[1:i+1]
        right_preorder = preorder[i+1:]
        root.left = self.construct(left_preorder, left_inorder)
        root.right = self.construct(right_preorder, right_inorder)
        return root