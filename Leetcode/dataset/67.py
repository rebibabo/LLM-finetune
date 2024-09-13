class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        if len(a) < len(b):
            a, b = b, a
        b = '0' * (len(a)-len(b)) + b
        carry = 0
        for i in range(len(a)-1, -1, -1):
            val = int(a[i]) + int(b[i]) + carry
            if val >= 2:
                carry = 1
            else:
                carry = 0
            res = str(val % 2) + res
        if carry:
            res = '1' + res
        return res