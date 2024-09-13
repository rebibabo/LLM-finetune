class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, word):
                    return True
        return False

    def dfs(self, i, j, word):
        if word == '':
            return True
        if i<0 or j<0 or i>=len(self.board) or j>=len(self.board[0]) or self.board[i][j] == '#':
            return False
        c = self.board[i][j]
        if c != word[0]:
            return False
        self.board[i][j] = '#'
        ret = False
        for di, dj in self.directions:
            ret |= self.dfs(i+di, j+dj, word[1:])
        self.board[i][j] = c
        return ret
