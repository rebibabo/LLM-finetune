class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0: 
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        l, r = newInterval
        i = 0
        ans = []
        while i < len(intervals) and l > intervals[i][1]:   
            ans.append(intervals[i])
            i += 1
        if i < len(intervals) and l >= intervals[i][0]:     
            lm = intervals[i][0]
        else:
            lm = l
        while i < len(intervals) and intervals[i][0] <= r:  
            i += 1
        i -= 1
        if i < len(intervals) and r <= intervals[i][1]:     
            rm = intervals[i][1]
        else:
            rm = r
        ans.append([lm, rm])
        ans += intervals[i+1:]
        return ans