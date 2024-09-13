class Solution:
    def zigzagLevelOrder(self, root):
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
                if pre % 2:
                    res.append(level[::-1])
                else:
                    res.append(level)
                pre = l
                level = []
            level.append(node.val)
            if node.left:
                q.put((node.left, l+1))
            if node.right:
                q.put((node.right, l+1))
        if l % 2:
            res.append(level[::-1])
        else:
            res.append(level)
        return res