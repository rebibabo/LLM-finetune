class Solution:
    def reverseBits(self, n: int) -> int:
        pows = [2**i for i in range(32)]
        ans = 0
        bits = []
        while n:
            bits.append(n % 2)
            n //= 2
        for i in range(len(bits)):
            ans += bits[i] * pows[len(bits) - i - 1]
        return ans * 2 ** (32 - len(bits))