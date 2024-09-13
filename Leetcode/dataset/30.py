class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        num, l = len(words), len(words[0])
        ans = []
        template_freq = {}
        for w in words:
            if w in template_freq:
                template_freq[w] += 1
            else:
                template_freq[w] = 1
        for i in range(l):
            str_freq = {}
            for j in range(num):
                new_word = s[i+j*l:i+(j+1)*l]
                if new_word in str_freq:
                    str_freq[new_word] += 1
                else:
                    str_freq[new_word] = 1
            if str_freq == template_freq:
                ans.append(i)
            for j in range(num, len(s) // l):
                old_word = s[i+(j-num)*l:i+(j-num+1)*l]
                new_word = s[i+j*l:i+(j+1)*l]
                if str_freq[old_word] == 1:
                    del str_freq[old_word]
                else:
                    str_freq[old_word] -= 1
                if new_word in str_freq:
                    str_freq[new_word] += 1
                else:
                    str_freq[new_word] = 1
                if str_freq == template_freq:
                    ans.append(i + (j-num+1) * l)
        return ans