"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        nodeHash = {None : None}
        
        
        cpy_head = Node(x = head.val)
        nodeHash[head] = cpy_head

        cur = head.next

        while cur:
            newNode = Node(x = cur.val)
            nodeHash[cur] = newNode
            cur = cur.next

        cur = head

        while cur:
            nodeHash[cur].next = nodeHash[cur.next]
            nodeHash[cur].random = nodeHash[cur.random]

            cur = cur.next
        
        return cpy_head
        

