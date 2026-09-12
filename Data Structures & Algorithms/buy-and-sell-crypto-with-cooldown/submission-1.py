class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Idea: We need to consider if we have a neetcoin or not.
        # If we have one, we can either sell or not sell. If we sell, we must consider day + 2.
        # If we do not have one, we can buy or not buy.
        
        # Probably easier to start from the beginning i.e. tabulation here.
        # If we choose to buy, we consider max from sell two days ago? 
        # If we choose to sell, we 

        # Ok base cases. If we are at the end and it is a buy, we do nothing. If sell, must sell.
        # On the second last one, we could basically take profit - buy and go to next for sell.
        # I guess the dp is day and state, and the value is the max current money.
        memo = {}
        def solve(day, owned):
            # Base cases
            if day >= len(prices):
                return 0
            if day == len(prices) - 1:
                if owned:
                    return prices[day]
                else:
                    return 0
            
            if (day, owned) in memo:
                return memo[(day, owned)]

            if owned:
                memo[day, owned] = max(solve(day + 1, True), prices[day] + solve(day + 2, False))  
            else:
                memo[day, owned] = max(solve(day + 1, True) - prices[day], solve(day + 1, False))
            return memo[day, owned]
        return solve(0, False)
