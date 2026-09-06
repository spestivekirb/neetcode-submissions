# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_hash = {}
        for i in range(len(inorder)):
            inorder_hash[inorder[i]] = i 
        
        def constructTree(cur, left, right):
            if left > right or left < 0 or right >= len(inorder):
                return None
           
            pos = inorder_hash[preorder[cur]]

            leftChild = constructTree(cur + 1, left, pos - 1)
            rightChild = constructTree(cur + pos - left + 1, pos + 1, right)

            return TreeNode(val=preorder[cur], left=leftChild, right=rightChild)
            

        

        return constructTree(0, 0, len(inorder) - 1)

        