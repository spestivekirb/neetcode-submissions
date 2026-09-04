# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        l_tree = root.left
        r_tree = root.right

        root.left = self.invertTree(r_tree)
        root.right = self.invertTree(l_tree)


        return root