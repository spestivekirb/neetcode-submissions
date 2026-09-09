# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret = []
        q = collections.deque()
        q.append(root)
        while q:
            cur = q.popleft()
            if cur is None:
                ret.append("N#")
            else:
                ret.append(str(cur.val) + "#")
                q.append(cur.left)
                q.append(cur.right)
        return "".join(ret)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def valend(index):
            while data[index] != "#":
                index += 1
            return index

        end = valend(0)
        first = data[0:valend(0)]
        if first == "N":
            return None
        
        root = TreeNode(first)
        i = valend(0) + 1
        q = collections.deque()
        q.append(root)

        while i < len(data):
            cur = q.popleft()
            leftend = valend(i)
            left = data[i:leftend]
            if left == "N":
                cur.left = None
            else:
                l = TreeNode(int(left))
                cur.left = l
                q.append(l)
            i = leftend + 1

            rightend = valend(i)
            right = data[i:rightend]
            if right == "N":
                cur.right = None
            else:
                r = TreeNode(int(right))
                cur.right = r
                q.append(r)
            i = rightend + 1
        return root
            



        


        

