class Solution:
    def add_freq(self, freq, c):
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1

    def check(self, f1, f2):
        if len(f1) < len(f2):
            return True
        for k in f1:
            if f1[k] < f2[k]:
                return True
        return False

    def minWindow(self, s: str, t: str) -> str:
        l, template_freq, freq = len(t), {}, {}
        for i in range(l):
            self.add_freq(template_freq, t[i])
        min_length, min_str, j = 10e5, "", 0
        for i in range(len(s)):
            while j < len(s) and self.check(freq, template_freq):
                if s[j] in template_freq:
                    self.add_freq(freq, s[j])
                j += 1
            if j - i < min_length and not self.check(freq, template_freq):
                min_str = s[i:j]
                min_length = j - i
            if s[i] in freq:
                if freq[s[i]] == 1:
                    del freq[s[i]]
                else:
                    freq[s[i]] -= 1
        return min_str