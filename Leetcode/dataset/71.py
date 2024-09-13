class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        path = [p for p in path if p not in ['', '.']]
        stack = []
        for p in path:
            if p == '..':   
                if not stack:   
                    continue
                stack.pop()     
            else:
                stack.append(p) 
        return '/' + '/'.join(stack)