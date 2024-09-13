class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.root = root
        path1 = self.findPath(p)
        path2 = self.findPath(q)
        if len(path1) > len(path2):
            path1, path2 = path2, path1
        diff = len(path2) - len(path1)
        for each in path1:
            print(each.val, end='')
        print()
        for each in path2:
            print(each.val, end='')
        path2 = path2[diff:]
        i = 0
        while i < len(path1) and path1[i] != path2[i]:
            i += 1
        return path1[i]

    def findPath(self, target):
        path = []
        def dfs(root, target):
            if not root:
                return False
            if root == target:
                return True
            if dfs(root.left, target) or dfs(root.right, target):
                path.append(root)
                return True
            return False
        dfs(self.root, target)
        return [target] + path