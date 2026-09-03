# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev = None
        cur = head
        next = head.next
        while next is not None:
            cur.next = prev
            prev = cur
            cur = next
            next = cur.next
        cur.next = prev
        return cur