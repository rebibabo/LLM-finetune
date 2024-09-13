class Solution:
    def add(self, n):
        res = 0
        while n:
            res += (n % 10) ** 2
            n //= 10
        return res

    def isHappy(self, n: int) -> bool:
        max_time = 100
        for _ in range(max_time):
            n = self.add(n)
            if n == 1:
                return True
        return False