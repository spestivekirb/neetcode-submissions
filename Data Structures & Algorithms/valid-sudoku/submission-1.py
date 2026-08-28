class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = [set() for _ in range(9)]
        colHash = [set() for _ in range(9)]
        boxHash = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue

                if val in rowHash[row]:
                    return False
                else:
                    rowHash[row].add(val)
                
                if val in colHash[col]:
                    return False
                else:
                    colHash[col].add(val)
                
                box = (row // 3) * 3 + (col // 3)

                if val in boxHash[box]:
                    return False
                else:
                    boxHash[box].add(val)

        return True
