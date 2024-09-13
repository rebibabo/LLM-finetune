class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            bits = self.int2bit(n)
        else:
            bits = self.int2bit(-n)
        pow = [x]
        for _ in range(len(bits)-1):
            pow.append(pow[-1] * pow[-1])
        ans = 1
        for i in range(len(bits)):
            if bits[i] == 1:
                ans *= pow[i]
        return ans if n > 0 else 1 / ans

    def int2bit(self, n):
        bits = []
        while n:
            bits.append(n%2)
            n //= 2
        return bits