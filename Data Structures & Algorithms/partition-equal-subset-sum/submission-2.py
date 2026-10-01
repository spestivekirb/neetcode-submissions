class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Idea: We know sum of nums. If sum is odd we know false fs.
        # If even, we need to find a subset that adds up to half.
        # We probably dont need to scan the whole space, can memo this.
        # Ok so brute force is for each try include and exclude and see if matches?
        # Ig see if we can meet target 

        target = sum(nums)
        if target % 2 == 1:
            return False
        else:
            target //= 2
        memo = {}

        def solve(index, remaining):
            if remaining == 0:
                return True
            if remaining < 0:
                return False
            if index >= len(nums):
                return False
            if (index, remaining) in memo:
                return memo[(index, remaining)]
            
            memo[(index, remaining)] = solve(index + 1, remaining - nums[index]) or solve(index + 1, remaining)
            return memo[(index, remaining)]
        
        return solve(0, target)
            