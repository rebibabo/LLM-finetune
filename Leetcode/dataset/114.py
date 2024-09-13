class Solution:
    def flatten(self, root) -> None:

        while root:
            if root.left:
                pred = next = root.left
                while next.right:
                    next = next.right
                next.right = root.right
                root.left = None
                root.right = pred
            root = root.right