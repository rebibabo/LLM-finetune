class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        l = len(triangle)
        dp = [[0 for _ in range(i+1)] for i in range(l)]
        dp[0][0] = triangle[0][0]
        for i in range(1, l):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        for i in range(2, l):
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        res = float("inf")
        for i in range(l):
            if dp[-1][i] < res:
                res = dp[-1][i]
        return res