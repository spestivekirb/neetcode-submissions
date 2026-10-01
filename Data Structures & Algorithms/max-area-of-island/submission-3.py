class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSize = 0

        n = len(grid)
        m = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(row, col):
            if row < 0 or col < 0 or row >= n or col >= m:
                return 0
            if grid[row][col]:
                grid[row][col] = 0
                total = 1
                for dr, dc in directions:
                    total += dfs(row + dr, col + dc)
                return total
            else:
                return 0

        
        for row in range(n):
            for col in range(m):
                if grid[row][col]:
                    maxSize = max(maxSize, dfs(row, col))
        return maxSize