class MinStack:
    def __init__(self):
        self.austack = []   
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.austack or val <= self.austack[-1]:
            self.austack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.austack[-1]:
            self.austack.pop()
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.austack:
            return self.austack[-1]
        return self.stack[-1]