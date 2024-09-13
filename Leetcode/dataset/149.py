class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        self.points = sorted(points, key = lambda x:x[0])
        self.max_num = 1
        self.inf = float("inf")
        self.lines = set()
        for i, (x, y) in enumerate(self.points):
            self.calculate(x, y, i)
        return self.max_num

    def calculate(self, x, y, i):
        points = self.points[i+1:]
        for j, (x_, y_) in enumerate(points):
            num = 2
            new_points = points[:j] + points[j+1:]
            if x == x_:
                if (self.inf, x) not in self.lines:
                    self.lines.add((self.inf, x))
                    for _x, _y in new_points:
                        if _x == x:
                            num += 1
            elif y == y_:
                if (0, y) not in self.lines:
                    self.lines.add((0, y))
                    for _x, _y in new_points:
                        if _y == y:
                            num += 1
            else:
                k = (y-y_) / (x-x_)
                b = y - k*x
                if (k, b) not in self.lines:
                    self.lines.add((k, b))
                    for _x, _y in new_points:
                        if (x - x_) * (y - _y) == (y - y_) * (x - _x):
                            num += 1
            if self.max_num < num:
                self.max_num = num