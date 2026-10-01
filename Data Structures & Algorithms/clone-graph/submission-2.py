"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}
        if node == None:
            return None

        def dfs(node):
            newnode = Node(node.val)
            nodes[node.val] = newnode

            for n in node.neighbors:
                if n.val in nodes:
                    newnode.neighbors.append(nodes[n.val])
                else:
                    newnode.neighbors.append(dfs(n))

            return newnode
        return dfs(node)