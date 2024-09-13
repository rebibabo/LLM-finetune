class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        outer_iter = l // 2
        for i in range(outer_iter):
            for j in range(l - 1 - 2*i): 
                matrix[i][i+j], matrix[i+j][l-i-1], matrix[l-i-1][l-i-j-1], matrix[l-i-j-1][i] = matrix[l-i-j-1][i], matrix[i][i+j], matrix[i+j][l-i-1], matrix[l-i-1][l-i-j-1]