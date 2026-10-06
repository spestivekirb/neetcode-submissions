# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # From a root, we need to determine the longest path in the left subtree and the longest path in the right subtree.
        # From there, the path is lefth + righth

        def dfs(node):
            if node is None:
                return 0, 0
            
            lefth, leftd = dfs(node.left)
            righth, rightd = dfs(node.right)

            return 1 + max(lefth, righth), max(lefth + righth, leftd, rightd)
        
        return dfs(root)[1]
