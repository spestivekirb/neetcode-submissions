# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1
        def dfs(root):
            nonlocal count
            if root.left:
                res = dfs(root.left)
                if res is not None:
                    return res
            
            print(root.val)
            if count == k:
                return root.val
            count += 1

            if root.right:
                return dfs(root.right)
        
        return dfs(root)
        