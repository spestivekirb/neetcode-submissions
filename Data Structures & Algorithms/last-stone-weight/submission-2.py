class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-num for num in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            stone1 = -heapq.heappop(maxheap)
            stone2 = -heapq.heappop(maxheap)

            diff = stone1 - stone2

            if diff != 0:
                heapq.heappush(maxheap, -diff)

        
        if maxheap:
            return -maxheap[0]
        else:
            return 0
        