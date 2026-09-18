class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # If we transpose the matrix, diagonal flip.
        # If we flip the matrix 
        # 1 2 3     7 8 9       7 4 1
        # 4 5 6     4 5 6       8 5 2
        # 7 8 9     1 2 3       9 6 3

        n = len(matrix)
        for i in range(math.ceil(n/2)):
            matrix[i], matrix[n-i - 1] = matrix[n - i - 1], matrix[i]
        
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        