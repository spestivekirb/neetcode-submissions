class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowl = 0
        rowr = len(matrix) - 1
        rowm = 0
        while rowl < rowr:
            rowm = (rowl + rowr) // 2
            if matrix[rowm][-1] < target:
                rowl = rowm + 1
            else:
                rowr = rowm

        coll = 0
        colr = len(matrix[rowl]) - 1
        while coll <= colr:
            colm = (coll + colr) // 2
            if matrix[rowl][colm] == target:
                return True
            elif matrix[rowl][colm] < target:
                coll = colm + 1
            else:
                colr = colm - 1
        
        return False
            