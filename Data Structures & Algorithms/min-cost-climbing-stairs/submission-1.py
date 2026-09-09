class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(dp)):
            dp[i] = min(cost[i-2] + dp[i-2], cost[i-1] + dp[i-1])
        return dp[-1]

        