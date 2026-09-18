class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lb, ub = 0, 0
        rb = len(matrix[0])
        db = len(matrix)

        res = []

        while lb < rb and ub < db:
            if lb < rb and ub < db:
                for i in range(lb, rb):
                    res.append(matrix[ub][i])
                ub += 1
            
            if lb < rb and ub < db:
                for j in range(ub, db):
                    res.append(matrix[j][rb-1])
                rb -= 1
            
            if lb < rb and ub < db:
                for k in range(rb - 1, lb - 1, -1):
                    res.append(matrix[db-1][k])
                db -= 1
            
            if lb < rb and ub < db:
                for l in range(db - 1, ub - 1, -1):
                    res.append(matrix[l][lb])
                lb += 1
        return res

