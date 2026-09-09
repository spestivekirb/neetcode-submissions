class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        p_visited = set()

        # Pacific Loop
        q = collections.deque()
        for i in range(len(heights)):
            p_visited.add((i, 0))
            q.append((i, 0))

        if len(heights[0]) > 1:
            for j in range(1, len(heights[0])):
                p_visited.add((0, j))
                q.append((0, j))
        
        while q:
            row, col = q.popleft()
            
            for dx, dy in directions:
                nx = row + dx
                ny = col + dy

                if nx >= 0 and ny >= 0 and nx < len(heights) and ny < len(heights[0]):
                    if (nx, ny) not in p_visited and heights[nx][ny] >= heights[row][col]:
                        p_visited.add((nx, ny))
                        q.append((nx, ny))


        a_visited = set()
        # Atlantic Loop
        for i in range(len(heights)):
            a_visited.add((i, len(heights[0]) - 1))
            q.append((i, len(heights[0]) - 1))

        if len(heights[0]) > 1:
            for j in range(0, len(heights[0]) - 1):
                a_visited.add((len(heights) - 1, j))
                q.append((len(heights) - 1, j))
        
        while q:
            row, col = q.popleft()
            
            for dx, dy in directions:
                nx = row + dx
                ny = col + dy

                if (nx, ny) not in a_visited and nx >= 0 and ny >= 0 and nx < len(heights) and ny < len(heights[0]):
                    if heights[nx][ny] >= heights[row][col]:
                        a_visited.add((nx, ny))
                        q.append((nx, ny))
            
        return list(p_visited & a_visited)
