class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        min, max = 10e5, -1
        mins = []
        for i in range(l):
            if min > prices[i]:
                min = prices[i]
            mins.append(min)
        res = 0
        for i in range(l-1, -1, -1):
            if max < prices[i]:
                max = prices[i]
            if max - mins[i] > res:
                res = max - mins[i]
        return res