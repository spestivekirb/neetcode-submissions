class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Idea: If we select something convert its pos on board to "."
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def solve(row, col, index):
            if index >= len(word):
                return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            if board[row][col] == word[index]:
                board[row][col] = "."
                for d in directions:
                    if solve(row + d[0], col + d[1], index + 1):
                        return True
                board[row][col] = word[index]
                return False
            else:
                return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if solve(row, col, 0):
                    return True
        return False
