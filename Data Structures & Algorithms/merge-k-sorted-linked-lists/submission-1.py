# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dhead = ListNode()
        tail = dhead
        heap = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i]]
        heapq.heapify(heap)

        while heap:
            _, i, nextNode = heapq.heappop(heap)
            tail.next = nextNode
            tail = tail.next
            if nextNode.next is not None:
                heapq.heappush(heap, (nextNode.next.val, i, nextNode.next))

        return dhead.next