class Solution:
    def sumNumbers(self, root) -> int:
        return self.calculate(root)
    
    def calculate(self, root):
        ans, path = [0], ''
        def dfs(root, path, ans):
            if not root:
                return 
            path += str(root.val)
            if not root.left and not root.right:
                ans[0] += int(path)
            else:
                dfs(root.left, path, ans)
                dfs(root.right,path, ans)
            path = path[:-1]
        dfs(root, path, ans)
        return ans[0]