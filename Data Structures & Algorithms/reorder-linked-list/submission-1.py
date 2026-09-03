# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Split the list in two

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # When this terminates, slow is at middle index

        prev = slow
        cur = slow.next

        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        tail = prev
        

        while head:
            temp = head.next
            head.next = tail
            if not tail:
                return
            tail = tail.next
            head.next.next = temp
            head = temp
        