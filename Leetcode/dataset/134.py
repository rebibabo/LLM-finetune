class Solution:
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_sum, cost_sum, max_diff, idx = 0, 0, -10e6, 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            gas_sum += g
            cost_sum += c
            diff = cost_sum - gas_sum
            if diff >= max_diff:    
                max_diff = diff
                idx = i
        if cost_sum > gas_sum:
            return -1
        return (idx+1)%len(gas)