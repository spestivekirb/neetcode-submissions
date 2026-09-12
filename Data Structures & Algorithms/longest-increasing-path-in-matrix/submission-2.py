class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # The thing we memo is the longest path starting from that pos I think.
        maxpath = 0
        memo = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        # We never consider path since it must be strictly increasing
        def dfs(x, y, prev):
            if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
                return 0
            if matrix[x][y] <= prev:
                return 0
            if memo[x][y] != 0:
                return memo[x][y]
            longest = 0
            for dx, dy in directions:
                longest = max(longest, dfs(x + dx, y + dy, matrix[x][y]))
            memo[x][y] = 1 + longest
            return memo[x][y]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if memo[row][col] == 0:
                    dfs(row, col, -1)

        return max(max(row) for row in memo)