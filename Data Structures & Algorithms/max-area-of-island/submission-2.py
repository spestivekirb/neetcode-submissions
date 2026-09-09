class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0
            if not grid[row][col]:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    maxArea = max(maxArea, dfs(row, col))



        return maxArea