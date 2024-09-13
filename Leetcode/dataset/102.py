class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        from queue import Queue
        q = Queue()
        res, level = [], []
        pre = 0
        q.put((root, 0))
        while not q.empty():
            node, l = q.get()
            if l != pre:
                pre = l
                res.append(level)
                level = []
            level.append(node.val)
            if node.left:
                q.put((node.left, l+1))
            if node.right:
                q.put((node.right, l+1))
        res.append(level)
        return res