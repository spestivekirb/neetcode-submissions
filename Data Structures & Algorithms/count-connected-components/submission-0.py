class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Idea: Can we just count the number of times we could run a dfs?
        edgeDict = collections.defaultdict(list)
        for edge in edges:
            edgeDict[edge[0]].append(edge[1])
            edgeDict[edge[1]].append(edge[0])
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in edgeDict[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        return components