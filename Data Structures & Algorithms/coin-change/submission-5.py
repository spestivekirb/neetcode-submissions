class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # At a given case, we should consider 1 + cur - each coin

        memo = {0:0}
        def recursive(remaining):
            if remaining in memo:
                return memo[remaining]
   
            if remaining < min(coins):
                return float("inf")
            
            possible = []
            for coin in coins:
                possible.append(recursive(remaining - coin))
            
            memo[remaining] = 1 + min(possible)
            return memo[remaining]

        ans = recursive(amount)
        
        if ans == float('inf'):
            return -1
        else:
            return ans
