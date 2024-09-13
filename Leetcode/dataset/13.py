class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        special = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        res, i = 0, 0
        while i < len(s):
            if s[i] in ['I', 'X', 'C']:
                if s[i:i+2] in special:
                    res += special[s[i:i+2]]
                    i += 2
                    continue
            res += dict[s[i]]
            i += 1
        return res