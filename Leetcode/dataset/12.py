class Solution:
    def intToRoman(self, num: int) -> str:
        thousand = {1:'M', 2:'MM', 3:'MMM'}
        hundred = {1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'}
        ten = {1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'}
        one = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
        res = ''
        if num // 1000 != 0:
            res += thousand[num // 1000]
            num %= 1000
        if num // 100 != 0:
            res += hundred[num // 100]
            num %= 100
        if num // 10 != 0:
            res += ten[num // 10]
            num %= 10
        if num != 0:
            res += one[num]
        return res