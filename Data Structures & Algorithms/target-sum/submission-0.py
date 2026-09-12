class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Ok so base case: If we are out of nums, then return 1 if total is target, else return 0.
        # Dp because we do dp on position in nums and the total.
        # We return the sum of num of ways to reach the target if we add here and if we sub here.

        memo = {}

        def solve(index, total):
            if index >= len(nums):
                return total == target
            if (index, total) in memo:
                return memo[(index, total)]

            memo[(index, total)] = solve(index + 1, total + nums[index]) + solve(index + 1, total - nums[index])
            return memo[(index, total)]
        
        return solve(0, 0)
        