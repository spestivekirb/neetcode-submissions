class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, i):
        if self.par[i] == i:
            return i    
        else:
            self.par[i] = self.find(self.par[i])
            return self.par[i]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return
        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu
        self.par[pv] = pu
        if self.rank[pu] == self.rank[pv]:
            self.rank[pu] += 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def calculatedist(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1]) 
        edges = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                edges.append((calculatedist(points[i], points[j]), i, j))
        
        edges.sort()
        
        dsu = DSU(len(points))
        total = 0
        for edge in edges:
            
            if dsu.find(edge[1]) != dsu.find(edge[2]):
                print(edge)
                dsu.union(edge[1], edge[2])
                total += edge[0]

        return total
        