"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = {node.val : Node(node.val)}
        def dfs(cur):
            clone = visited[cur.val]
            for child in cur.neighbors:
                if child.val in visited:
                    clone.neighbors.append(visited[child.val])
                else:
                    new = Node(child.val)
                    clone.neighbors.append(new)
                    visited[child.val] = new
                    dfs(child)
        dfs(node)
        return visited[node.val]
                    
                    
            

        