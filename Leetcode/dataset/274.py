class Solution:
    
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        l = len(citations)
        for i in range(len(citations)):
            if citations[i] >= l - i:
                return l - i
        return 0