class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, i):
        if self.par[i] == i:
            return i
        self.par[i] = self.find(self.par[i])
        return self.par[i]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False

        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa
        self.par[pb] = pa
        
        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res

