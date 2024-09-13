class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = [0] * 128
        length, max_length, j = 0, 0, 0
        for i in range(len(s)):
            while j < len(s) and charset[ord(s[j])] != 1:
                length += 1
                charset[ord(s[j])] = 1
                j += 1
            if length > max_length:
                max_length = length
            length -= 1
            charset[ord(s[i])] = 0
        return max_length