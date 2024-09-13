class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ','')
        new_s = ''
        for c in s:
            if 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57:
                new_s += c
        s = new_s
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True