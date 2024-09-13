class Solution:
    def numIslands(self, grid) -> int:
        self.grid = grid
        self.m, self.n, num = len(grid[0]), len(grid), 0
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] != 2 and self.grid[i][j] == '1':
                    num += 1
                    self.spray(i, j)
        return num

    def spray(self, i, j):
        
        self.grid[i][j] = 2
        if i+1 < self.n and self.grid[i+1][j] == '1' and self.grid[i+1][j] != 2:
            self.spray(i+1, j)
        if j+1 < self.m and self.grid[i][j+1] == '1' and self.grid[i][j+1] != 2:
            self.spray(i, j+1)
        if j-1 >= 0 and self.grid[i][j-1] == '1' and self.grid[i][j-1] != 2:
            self.spray(i, j-1)
        if i-1 >= 0 and self.grid[i-1][j] == '1' and self.grid[i-1][j] != 2:
            self.spray(i-1, j)