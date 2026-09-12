class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # We need to form a subset that equals to half of target.
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2

        # Idea: Can we reach the target with the numbers so far
        memo = {}
        def solve(index, remaining):
            if (index, remaining) in memo:
                return memo[(index, remaining)]
            if index == len(nums):
                return remaining == 0
            
            memo[(index, remaining)] = solve(index + 1, remaining) or solve(index + 1, remaining - nums[index])
            return memo[(index, remaining)]


        return solve(0, target)
