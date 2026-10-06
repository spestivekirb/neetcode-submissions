# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        q = collections.deque()
        q.append(root)
        while q:
            empty = True
            for _ in range(2 ** depth):
                cur = q.popleft()
                if cur:
                    empty = False
                    q.append(cur.left)
                    q.append(cur.right)
                else:
                    q.append(None)
                    q.append(None)
            if empty:
                break
            else:
                depth += 1
        
        return depth