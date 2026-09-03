# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head

        while hare is not None:

            tortoise = tortoise.next

            try:
                hare = hare.next.next
            except:
                return False
            
            if tortoise == hare:
                return True

        return False