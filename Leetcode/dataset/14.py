class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        if len(strs) == 1:
            return strs[0]
        while True:
            flag = False
            for each in strs[1:]:
                if i >= len(each) or i >= len(strs[0]) or each[i] != strs[0][i]:
                    flag = True
                    break
            if flag:
                break
            i += 1
        return strs[0][:i]