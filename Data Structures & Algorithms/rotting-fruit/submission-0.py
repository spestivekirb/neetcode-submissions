class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotq = collections.deque()
        freshc = 0
        time = 0

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] 

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    freshc += 1
                elif grid[row][col] == 2:
                    rotq.append((row, col))
        
        while rotq and freshc > 0:
            timelen = len(rotq)
            for i in range(timelen):
                row, col = rotq.popleft()

                for dr, dc in directions:
                    trow = row + dr
                    tcol = col + dc
                    if trow in range(len(grid)) and tcol in range(len(grid[0])):
                        if grid[trow][tcol] == 1:
                            grid[trow][tcol] = 2
                            rotq.append((trow, tcol)) 
                            freshc -= 1


            time += 1


        
        if freshc:
            return -1
        return time
