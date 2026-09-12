class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # The state is the amount left and which coins are available.
        # Idea: We can chose to skip the current coin or not.
        # Base case: If amount is 0, return True. If coins empty and amount not 0, return False.

        memo = {}

        def solve(index, remaining):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            if index == len(coins):
                return 0
            
            if (index, remaining) in memo:
                return memo[(index, remaining)]

            memo[(index, remaining)] = solve(index, remaining - coins[index]) + solve(index + 1, remaining)
            return memo[(index, remaining)]
        return solve(0, amount)
