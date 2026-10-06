# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # OK but it is a binary serach tree. This makes it probably easier.
    # When we find an element that is between p and q, it has to be lca. More accurately, the first element between them (inclusive) when doing bfs
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        qu = collections.deque()
        qu.append(root)
        while qu:
            cur = qu.popleft()
            if (cur.val <= p.val and cur.val >= q.val) or (cur.val <= q.val and cur.val >= p.val):
                return cur
            else:
                if cur.left:
                    qu.append(cur.left)
                if cur.right:
                    qu.append(cur.right)