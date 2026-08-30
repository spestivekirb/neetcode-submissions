class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSeen = math.inf
        cur = 0

        maxProfit = 0

        while cur < len(prices):
            print(minSeen)
            maxProfit = max(maxProfit, prices[cur] - minSeen)
            minSeen = min(minSeen, prices[cur])
            cur += 1
        return maxProfit
        