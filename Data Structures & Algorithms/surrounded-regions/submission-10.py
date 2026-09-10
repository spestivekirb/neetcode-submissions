class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # If none exposed, flip all
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Edge case no interior
        if len(board) <= 2 or len(board[0]) <= 2:
            return

        def dfs(row, col):
            for dx, dy in directions:
                nx = row + dx
                ny = col + dy
                if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]):
                    continue
                if (nx, ny) not in visited and board[nx][ny] == "O":
                    visited.add((nx, ny))
                    dfs(nx, ny)
        
        for i in range(0, len(board)):
            if board[i][0] == 'O' and (i, 0) not in visited:
                visited.add((i, 0))
                dfs(i, 0)
            if board[i][len(board[0]) - 1] == 'O' and (i, len(board[0]) - 1) not in visited:
                visited.add((i, len(board[0]) - 1))
                dfs(i, len(board[0]) - 1)
        
        for j in range(0, len(board[0])):
            if board[0][j] == 'O' and (0, j) not in visited:
                visited.add((0, j))
                dfs(0, j)
            if board[len(board) - 1][j] == 'O' and (len(board) - 1, j) not in visited:
                visited.add((len(board) - 1, j))
                dfs(len(board) - 1, j)
        

        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) not in visited and board[row][col] == 'O':
                    board[row][col] = 'X'
                    
        