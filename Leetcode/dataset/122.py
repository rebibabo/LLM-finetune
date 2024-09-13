class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        min, max, res = prices[0], prices[0], 0
        for p in prices[1:]:
            if p <= max:
                res += max - min
                min = p
                max = p
            if p < min:
                min = p
            if p > max:
                max = p
        return res + max - min