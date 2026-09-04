class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def visit(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if grid[row][col] == "0":
                return
            if (row, col) in visited:
                return

            visited.add((row, col))

            visit(row+1, col)
            visit(row-1, col)
            visit(row, col+1)
            visit(row, col-1)

            

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    visit(row, col)
        return islands
            
        