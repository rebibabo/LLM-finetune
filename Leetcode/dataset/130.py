class Solution:
    
    def solve(self, board) -> None:
        self.board = board
        self.m, self.n = len(board), len(board[0])
        for i in range(0, self.m):
            if board[i][0] == 'O':
                self.dfs(i, 0)
            if board[i][-1] == 'O':
                self.dfs(i,self.n-1)
        for i in range(0, self.n):
            if board[0][i] == 'O':
                self.dfs(0, i)
            if board[-1][i] == 'O':
                self.dfs(self.m-1, i)
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] != 'I':
                    self.board[i][j] = 'X'
                else:
                    self.board[i][j] = 'O'
        
    def dfs(self, i, j):
        if self.board[i][j] != 'O':
            return
        self.board[i][j] = 'I'
        direction = [(0,1), (0,-1), (1,0), (-1,0)]
        for dx, dy in direction:
            if 0<=i+dx<self.m and 0<=j+dy<self.n and self.board[i+dx][j+dy] != 'I':
                self.dfs(i+dx, j+dy)