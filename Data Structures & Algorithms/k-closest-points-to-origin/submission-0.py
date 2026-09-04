class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = [(math.sqrt(p[0]**2 + p[1]**2), p[0], p[1]) for p in points]
        heapq.heapify(minheap)
        ans = []
        for _ in range(k):
            closest = heapq.heappop(minheap)
            ans.append([closest[1], closest[2]])
        return ans
