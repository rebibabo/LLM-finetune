class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        for c in magazine:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        for c in ransomNote:
            if c not in freq:
                return False
            if freq[c] == 1:
                del freq[c]
            else:
                freq[c] -= 1
        return True