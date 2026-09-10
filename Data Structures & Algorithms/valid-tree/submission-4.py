class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgedict = collections.defaultdict(list)

        if n == 1:
            return True
        for u, v in edges:
            edgedict[u].append(v)
            edgedict[v].append(u)
        for i in range(n):
            if i not in edgedict:
                return False

        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in edgedict[node].copy():
                if neighbor in visited:
                    return
                edgedict[node].remove(neighbor)
                edgedict[neighbor].remove(node)
                dfs(neighbor)
        
        dfs(0)

        for node in edgedict:
            if edgedict[node]:
                return False
        return True
