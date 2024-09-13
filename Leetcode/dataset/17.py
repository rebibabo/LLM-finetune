class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        if not digits:
            return res
        self.find(digits, '', res)
        return res

    def find(self, digits, str, res):
        if not digits:
            res.append(str)
            return 
        for c in self.map[digits[0]]:
            str += c
            self.find(digits[1:], str, res) 
            str = str[:-1]