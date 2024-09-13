class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        l, r = intervals[0]
        res = []
        for el, er in intervals[1:]:
            if el <= r:
                if er > r:
                    r = er
            else:
                res.append([l, r])
                l, r = el, er 
        res.append([l, r])
        return res