# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        rightview = []

        if root is None:
            return []
        while q:
            last = None
            for _ in range(len(q)):
                node = q.popleft()
                last = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            rightview.append(last.val)
        return rightview

        