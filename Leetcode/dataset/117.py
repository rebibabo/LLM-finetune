class Solution:
    def connect(self, root):
        if not root:
            return None
        from queue import Queue
        r, pre, pl, q = root, root, -1, Queue()
        q.put((root, 0))
        while not q.empty():
            root, l = q.get()
            if pl == l:
                pre.next = root
            else:
                pre.next = None
            pre, pl = root, l
            if root.left:
                q.put((root.left, l+1))
            if root.right:
                q.put((root.right, l+1))
        return r
        
    def test(self, root):
        ans = []
        while root:
            p = root
            while p:
                ans.append(p.val)
                p = p.next
            ans.append('#')
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = None
        return ans