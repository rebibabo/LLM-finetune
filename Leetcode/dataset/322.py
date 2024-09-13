class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = [0] * (amount + 1)
        for i in range(1, amount+1):
            _min = float("inf")
            for c in coins:
                if i - c >= 0 and _min > d[i - c] + 1:
                    _min = d[i - c] + 1
            d[i] = _min
        return -1 if d[-1] == float("inf") else d[-1]