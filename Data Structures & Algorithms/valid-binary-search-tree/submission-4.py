# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, minAllow, maxAllow):
            if root is None:
                return True
            
            if minAllow < root.val < maxAllow:
                return dfs(root.left, minAllow, root.val) and dfs(root.right, root.val, maxAllow)
            else:
                return False

        
        return dfs(root, -1000000001, 1000000001)

   

        