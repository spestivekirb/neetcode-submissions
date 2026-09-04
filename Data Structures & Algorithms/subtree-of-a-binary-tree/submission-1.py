# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkEquality(p, q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return checkEquality(p.left, q.left) and checkEquality(p.right, q.right)
            else:
                return False

        def solve(root, subRoot):
            if root is None:
                return not subRoot
            
            if root.val == subRoot.val:
                return checkEquality(root, subRoot) or solve(root.left, subRoot) or solve(root.right, subRoot)
            
            return solve(root.left, subRoot) or solve(root.right, subRoot)

        return solve(root, subRoot)




        