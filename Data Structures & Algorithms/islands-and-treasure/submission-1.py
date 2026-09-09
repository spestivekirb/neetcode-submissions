class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        visited = set()
        # Contains row, col, distance
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row, col, 0))
                    visited.add((row, col))

        adj = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while q:
            r, c, d = q.popleft()
            
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                continue
            if grid[r][c] == -1:
                continue
            grid[r][c] = d
            
            for dx, dy in adj:
                if (r+dx, c+dy) not in visited:
                    q.append((r + dx, c + dy, d + 1))
                    visited.add((r+dx, c+dy))
        

            

