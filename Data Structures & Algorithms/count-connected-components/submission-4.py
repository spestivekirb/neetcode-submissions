class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def find(self, i):
        if self.par[i] == i:
            return i
        self.par[i] = self.find(self.par[i])
        return self.par[i]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            self.par[pb] = pa
            return True
        return False

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res

