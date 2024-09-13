class Solution:
    def averageOfLevels(self, root):
        from queue import Queue
        q = Queue()
        res = []
        sum = 0
        num = 0
        pre = 0
        q.put((root, 0))
        while not q.empty():
            node, l = q.get()
            if l != pre:
                pre = l
                res.append(sum / num)
                sum = num = 0
            sum += node.val
            num += 1
            if node.left:
                q.put((node.left, l+1))
            if node.right:
                q.put((node.right, l+1))
        res.append(sum/num)
        return res