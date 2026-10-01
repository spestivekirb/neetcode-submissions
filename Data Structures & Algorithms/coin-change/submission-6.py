class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # I think dp is good to try here.

        if amount == 0:
            return 0

        dp = [10001] *(amount + 1)
        for i in range(amount + 1):
            if i in coins:
                dp[i] = 1
            for c in coins:
                if c < i:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        
        if dp[-1] == 10001:
            return -1
        else:
            return dp[-1]
