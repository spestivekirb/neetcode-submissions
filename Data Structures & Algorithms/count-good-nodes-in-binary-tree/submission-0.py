# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodCount = 0
        
        def dfs(root, maxSeen):
            nonlocal goodCount
            if root.val >= maxSeen:
                goodCount += 1
            
            if root.left:
                dfs(root.left, max(maxSeen, root.val))
            if root.right:
                dfs(root.right, max(maxSeen, root.val))
        
        dfs(root, -100)

        return goodCount
            
            
