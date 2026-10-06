# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Ok so idea is that each child must be balanced, through height.
        # Like a node itself must be balanced, and all subtrees need to be balanced.
        def dfs(node):
            if node == None:
                return 0, True
            lefth, leftbal = dfs(node.left)
            righth, rightbal = dfs(node.right)

            return 1 + max(lefth, righth), abs(lefth - righth) <= 1 and leftbal and rightbal
        
        return dfs(root)[1]