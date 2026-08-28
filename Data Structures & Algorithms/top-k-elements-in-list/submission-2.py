class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        for n, v in counts.items():
            freq[v].append(n)
        
        ans = []
        for i in range(len(freq)-1, 0, -1):
            ans.extend(freq[i])
            k -= len(freq[i])

            if k <= 0:
                return ans
        return ans