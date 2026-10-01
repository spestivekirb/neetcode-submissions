class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        islandCount = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return
            
            if grid[y][x] == "1":
                grid[y][x] = "0"
                for dx, dy in directions:
                    dfs(x + dx, y + dy)
            return

        
        for y in range(n):
            for x in range(m):
                if grid[y][x] == "1":
                    islandCount += 1
                    dfs(x, y)
        
        return islandCount
