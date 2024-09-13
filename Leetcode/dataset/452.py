class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[0])
        num, r = 1, points[0][1]
        for li, ri in points[1:]:
            if li <= r:
                if ri < r:
                    r = ri
            else:
                num += 1
                r = ri
        return num