# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Idea: A function should return itself + the max length between its two children trees, BUT we should keep track of max node + both children seperately.
        # We can also make the assumption that if the child path is negative, we can just disregard it.
        maxSum = float("-10000")
        def dfs(root):
            nonlocal maxSum
            if root is None:
                return 0
            
            l_child = max(dfs(root.left), 0)
            r_child = max(dfs(root.right), 0)

            maxSum = max(maxSum, root.val + l_child + r_child)

            return root.val + max(l_child, r_child)

        dfs(root)

        return maxSum



        