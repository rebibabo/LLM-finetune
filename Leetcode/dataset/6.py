class Solution:
    
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ''
        interval = 2 * numRows - 2
        for i in range(0, len(s), interval):
            res += s[i]
        for j in range(1, numRows - 1):
            i = 0
            while True:
                idx = j + interval * i
                if idx < len(s):
                    res += s[idx]
                else:
                    break
                idx = j - 2 * (j - 1) + 2 * (numRows - 2) + interval * i
                if idx < len(s):
                    res += s[idx]
                else:
                    break
                i += 1
        for i in range(numRows - 1, len(s), interval):
            res += s[i]
        return res